"""Unit tests for translate_readme — pure functions only (no API, no FS state)."""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent))
from _selector import (  # type: ignore[import-not-found]  # noqa: E402
    build_selector,
    inject_selector,
    strip_existing_selector,
)
from translate_readme import (  # noqa: E402
    file_hash,
    strip_outer_fence,
    validate_translation,
)


# ─── strip_outer_fence ──────────────────────────────────────────────────
class TestStripOuterFence:
    def test_no_fence_unchanged(self):
        text = "# Title\n\nBody paragraph.\n"
        assert strip_outer_fence(text).strip() == "# Title\n\nBody paragraph."

    def test_strips_markdown_fence(self):
        text = "```markdown\n# Title\nBody\n```"
        assert strip_outer_fence(text) == "# Title\nBody"

    def test_strips_plain_fence(self):
        text = "```\n# Title\n```"
        assert strip_outer_fence(text) == "# Title"

    def test_inner_fences_preserved(self):
        text = "# Title\n\n```bash\necho hi\n```\n\nMore text."
        out = strip_outer_fence(text)
        assert "```bash" in out
        assert "echo hi" in out


# ─── strip_existing_selector ────────────────────────────────────────────
class TestStripExistingSelector:
    def test_no_selector_unchanged(self):
        text = "# Title\n\nBody.\n"
        assert strip_existing_selector(text) == "# Title\n\nBody."

    def test_strips_english_marker(self):
        text = (
            "# Title\n"
            "\n"
            "**🌍 Read this in other languages:** [foo](bar.md)\n"
            "\n"
            "Body.\n"
        )
        out = strip_existing_selector(text)
        assert "Read this in other languages" not in out
        assert "Body." in out

    def test_strips_translated_selector_by_flag_signature(self):
        # Selector header translated to PT, flags survive
        text = (
            "# Título\n"
            "\n"
            "**🌍 Leia isto em outros idiomas:** [🇺🇸 English](../../README.md) • **🇧🇷 PT-BR** • [🇵🇹 PT-PT](README.pt-PT.md)\n"
            "\n"
            "Corpo.\n"
        )
        out = strip_existing_selector(text)
        assert "Leia isto em outros idiomas" not in out
        assert "Corpo." in out

    def test_strips_japanese_translated_selector(self):
        text = (
            "# タイトル\n"
            "\n"
            "**🌍 他の言語で読む:** [🇺🇸 English](../../README.md) • [🇧🇷 PT](README.pt-BR.md) • [🇯🇵 JA](README.ja.md)\n"
            "\n"
            "本文。\n"
        )
        out = strip_existing_selector(text)
        assert "他の言語で読む" not in out
        assert "本文。" in out


# ─── build_selector / inject_selector ───────────────────────────────────
class TestBuildSelector:
    def test_root_has_bold_english(self):
        sel = build_selector(current_lang=None)
        assert "🇺🇸 **English**" in sel
        assert ".github/i18n/README.pt-BR.md" in sel

    def test_translation_path_relative(self):
        sel = build_selector(current_lang="pt-BR")
        assert "[🇺🇸 English](../../README.md)" in sel
        assert "**🇧🇷 Português (BR)**" in sel
        # Other langs use sibling paths
        assert "[🇪🇸 Español](README.es.md)" in sel


class TestInjectSelector:
    def test_inserts_after_h1_with_blank_lines(self):
        content = "# Title\n\n![Badge](url)\n\nBody.\n"
        out = inject_selector(content, current_lang=None)
        lines = out.splitlines()
        # H1 at 0, blank at 1, selector at 2, blank at 3, badge at 4
        assert lines[0] == "# Title"
        assert lines[1] == ""
        assert "Read this in other languages" in lines[2]
        assert lines[3] == ""
        assert lines[4].startswith("![Badge]")

    def test_collapses_excess_blanks(self):
        content = "# Title\n\n\n\n\nBody.\n"
        out = inject_selector(content, current_lang=None)
        # No 4+ consecutive blanks
        assert "\n\n\n\n" not in out

    def test_idempotent_re_run(self):
        content = "# Title\n\nBody.\n"
        once = inject_selector(content, current_lang=None)
        twice = inject_selector(once, current_lang=None)
        assert once == twice


# ─── validate_translation ───────────────────────────────────────────────
class TestValidateTranslation:
    def test_identical_passes(self):
        src = "# Title\n\nBody with [link](#anchor).\n\n```py\nx=1\n```\n"
        assert validate_translation(src, src) == []

    def test_catches_missing_anchor(self):
        src = "[A](#one) [B](#two) [C](#three)"
        tgt = "[A](#one) [B](#two)"  # missing #three
        problems = validate_translation(src, tgt)
        assert any("missing anchors" in p for p in problems)

    def test_catches_code_fence_mismatch(self):
        src = "```py\nx=1\n```\n```sh\nls\n```\n"
        tgt = "```py\nx=1\n```\n"  # lost one block
        problems = validate_translation(src, tgt)
        assert any("code fence" in p for p in problems)

    def test_catches_short_output(self):
        src = "x" * 1000
        tgt = "x" * 100  # 10% of source
        problems = validate_translation(src, tgt)
        assert any("too short" in p for p in problems)


# ─── file_hash ──────────────────────────────────────────────────────────
class TestFileHash:
    def test_deterministic(self):
        assert file_hash("hello") == file_hash("hello")

    def test_different_inputs(self):
        assert file_hash("a") != file_hash("b")

    def test_unicode_handled(self):
        h = file_hash("# 🌟 タイトル\n\n中文 português")
        assert len(h) == 64  # sha256 hex


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))
