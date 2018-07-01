from mock import patch

from django.core.management import call_command
from django.test import TestCase

from publicdb.analysissessions.models import SessionRequest

from ..factories.analysissessions_factories import SessionRequestFactory
from ..factories.inforecords_factories import ClusterFactory


class TestManagement(TestCase):
    def setUp(self):
        super(TestManagement, self).setUp()

        cluster = ClusterFactory(number=0, country__number=0)

        # Newly created
        self.new = SessionRequestFactory(session_confirmed=False, session_pending=True, session_created=False, cluster=cluster)
        # Email confirmed
        self.confirmed = SessionRequestFactory(session_confirmed=True, session_pending=True, session_created=False, cluster=cluster)
        # Selected for create session
        self.selected = SessionRequestFactory(session_confirmed=False, session_pending=True, session_created=False, cluster=cluster)
        # Create session started
        self.started = SessionRequestFactory(session_confirmed=False, session_pending=False, session_created=False, cluster=cluster)
        # Session created
        self.created = SessionRequestFactory(session_confirmed=False, session_pending=False, session_created=True, cluster=cluster)

    @patch('publicdb.analysissessions.models.SessionRequest.create_session')
    def test_createsessions(self, mock_create_session):
        """The command only processes the confirmed session"""

        call_command('createsessions')
        mock_create_session.assert_called_once_with()
        self.confirmed.refresh_from_db()
        self.assertFalse(self.confirmed.session_confirmed)
