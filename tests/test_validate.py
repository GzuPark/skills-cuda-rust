import importlib.util
import subprocess
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('validate', Path(__file__).resolve().parents[1] / 'scripts' / 'validate.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class ValidationTests(unittest.TestCase):
    def test_valid_skill_and_missing_source_are_distinguished(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / 'skills'
            source = Path(temp) / 'source'
            (root / 'example').mkdir(parents=True)
            source.mkdir()
            subprocess.run(['git', 'init', '-q', str(source)], check=True)
            subprocess.run(['git', '-C', str(source), 'config', 'user.email', 'test@example.com'], check=True)
            subprocess.run(['git', '-C', str(source), 'config', 'user.name', 'Test'], check=True)
            (source / 'guide.md').write_text('guide\n')
            subprocess.run(['git', '-C', str(source), 'add', 'guide.md'], check=True)
            subprocess.run(['git', '-C', str(source), 'commit', '-qm', 'guide'], check=True)
            rev = subprocess.check_output(['git', '-C', str(source), 'rev-parse', 'HEAD'], text=True).strip()
            index = root / 'llms.txt'
            index.write_text(f'# Test\n\n[Guide](https://github.com/NVIDIA/cuda-rust/blob/{rev}/guide.md)\n')
            skill = root / 'example' / 'SKILL.md'
            skill.write_text('---\nname: example\ndescription: Example skill.\n---\n\n# Example\n')
            self.assertEqual(validator.validate(root, source)[0], [])
            index.write_text(index.read_text().replace('guide.md', 'missing.md'))
            self.assertTrue(any('Missing NVIDIA source' in error for error in validator.validate(root, source)[0]))
            skill.write_text(skill.read_text().replace('name: example', 'name: incorrect'))
            self.assertTrue(any('invalid skill name' in error for error in validator.validate(root, source)[0]))


if __name__ == '__main__':
    unittest.main()
