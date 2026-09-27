import importlib.util
import pathlib
import unittest

spec = importlib.util.spec_from_file_location('context_hook', pathlib.Path(__file__).with_name('codex-session-context.py'))
hook = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hook)


class ContextHookTest(unittest.TestCase):
    def test_start_sources(self):
        for source in ['startup', 'resume', 'compact', 'clear']:
            result = hook.response({'hook_event_name': 'SessionStart', 'source': source})
            self.assertEqual(result['hookSpecificOutput']['hookEventName'], 'SessionStart')
            self.assertTrue(result['hookSpecificOutput']['additionalContext'])
            self.assertNotIn('decision', result)

    def test_other_events_do_not_get_session_context(self):
        self.assertEqual(hook.response({'hook_event_name': 'PreToolUse'}), {})


if __name__ == '__main__':
    unittest.main()
