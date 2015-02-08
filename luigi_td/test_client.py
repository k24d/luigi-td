from client import ResultProxy
from test_helper import MockJob

from unittest import TestCase
from nose.tools import eq_, raises

import tempfile

class ResultProxyTestCase(TestCase):
    SUCCESS_JOB = {
        'job_id': 1,
        'status': 'success',
        'size': 20,
        'description': [['cnt', 'int']],
        'rows': [[5000]],
    }

    def test_with_successful_job(self):
        result = ResultProxy(MockJob(self.SUCCESS_JOB))
        eq_(result.job_id, self.SUCCESS_JOB['job_id'])
        eq_(result.status, self.SUCCESS_JOB['status'])
        eq_(result.size, self.SUCCESS_JOB['size'])
        eq_(result.description, self.SUCCESS_JOB['description'])
        eq_(list(result), self.SUCCESS_JOB['rows'])
        with tempfile.NamedTemporaryFile() as f:
            result.to_csv(f.name)
            eq_(f.read(), "cnt\n5000\n")