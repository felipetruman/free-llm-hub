"""Unit and local integration tests for README translations (no provider API)."""
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


class TestDiscoverySync:
    @staticmethod
    def setup_docs(path):
        i18n = path / ".github" / "i18n"
        i18n.mkdir(parents=True)
        repo = Path(__file__).resolve().parents[2]
        for src in (repo / ".github" / "i18n").iterdir():
            (i18n / src.name).write_bytes(src.read_bytes())
        source = path / "README.md"
        source.write_bytes((repo / "README.md").read_bytes())
        return source, i18n

    @staticmethod
    def render_snapshot(path, source, *, editorial_change=False):
        import os
        import shutil
        import subprocess

        repo = Path(__file__).resolve().parents[2]
        shutil.copytree(repo / "scripts", path / "scripts")
        shutil.copytree(repo / "data", path / "data")
        # git history and provider credentials are not needed to render a local snapshot.
        (path / "data" / "discovered_models.json").write_text(
            '{"openrouter":{"status":"ok","count":42},'
            '"groq":{"status":"auth_required_401","count":0},'
            '"kluster":{"status":"error_ConnectError","count":0}}',
            encoding="utf-8",
        )
        if editorial_change:
            old = source.read_text(encoding="utf-8").replace("community-driven", "curated")
            source.write_text(old, encoding="utf-8")
            (path / ".github/i18n/.source-hash").write_text(file_hash(old), encoding="utf-8")
        subprocess.run(
            [sys.executable, str(path / "scripts/render_readme.py")],
            check=True,
            cwd=path,
            env={key: value for key, value in os.environ.items() if key != "GEMINI_API_KEY"},
        )

    def test_snapshot_change_updates_all_locale_tables_and_source_hash(self, tmp_path):
        source, i18n = self.setup_docs(tmp_path)
        self.render_snapshot(tmp_path, source)

        translations = list(i18n.glob("README.*.md"))
        assert len(translations) == 6
        for translation in translations:
            updated = translation.read_text(encoding="utf-8")
            assert "| `openrouter` | 42 | `https://openrouter.ai/api/v1` |" in updated
            assert "| `groq` | auth_required_401 |" in updated
            assert "| `kluster` | error_ConnectError |" in updated
            assert "| `openrouter` | 358 |" not in updated
            original = Path(__file__).resolve().parents[2] / ".github" / "i18n" / translation.name
            assert updated.split("## 🔍 ", 1)[0] == original.read_text(encoding="utf-8").split("## 🔍 ", 1)[0]

        assert (i18n / ".source-hash").read_text(encoding="utf-8").strip() == file_hash(source.read_text(encoding="utf-8"))

    def test_change_outside_snapshot_does_not_advance_hash(self, tmp_path):
        source, i18n = self.setup_docs(tmp_path)
        translated = i18n / "README.pt-BR.md"
        before = translated.read_bytes()
        self.render_snapshot(tmp_path, source, editorial_change=True)

        assert translated.read_bytes() == before
        assert (i18n / ".source-hash").read_text(encoding="utf-8").strip() != file_hash(source.read_text(encoding="utf-8"))

    def test_missing_translation_does_not_advance_hash_or_rewrite_other_locales(self, tmp_path):
        source, i18n = self.setup_docs(tmp_path)
        (i18n / "README.ja.md").unlink()
        translated = i18n / "README.es.md"
        before = translated.read_bytes()
        self.render_snapshot(tmp_path, source)

        assert translated.read_bytes() == before
        assert (i18n / ".source-hash").read_text(encoding="utf-8").strip() != file_hash(source.read_text(encoding="utf-8"))
