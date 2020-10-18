from django.test import TransactionTestCase, RequestFactory
from django.contrib.auth.models import User
from django.contrib.admin.sites import AdminSite
from django_q.models import OrmQ

from municipal_finance.admin import (
    MunicipalityProfilesRebuildAdmin,
    MunicipalityStaffContactsUploadAdmin,
    CashflowUpdateAdmin,
)
from municipal_finance.models import (
    MunicipalityStaffContactsUpload,
    MunicipalityProfilesRebuild,
    CashflowUpdate,
)


class MunicipalityProfileRebuildAdminTestCase(TransactionTestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username='super',
            email='super@email.org',
            password='pass',
        )
        self.model_admin = MunicipalityProfilesRebuildAdmin(
            model=MunicipalityStaffContactsUpload,
            admin_site=AdminSite(),
        )

    def test_save_task_trigger(self):
        request = self.factory.get(
            '/admin/municipal_finance/municipalityprofilesrebuild/add/'
        )
        request.user = self.user
        obj = MunicipalityStaffContactsUpload()
        self.model_admin.save_model(
            obj=obj,
            request=request,
            form=None,
            change=None,
        )
        self.assertEquals(obj.user, self.user)
        record = OrmQ.objects.latest('id')
        self.assertEquals(
            record.func(),
            'municipal_finance.compile_data.compile_data',
        )


class MunicipalityStaffContactsUploadTestCase(TransactionTestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username='super',
            email='super@email.org',
            password='pass',
        )
        self.model_admin = MunicipalityStaffContactsUploadAdmin(
            model=MunicipalityStaffContactsUpload,
            admin_site=AdminSite(),
        )

    def test_save_task_trigger(self):
        request = self.factory.get(
            '/admin/municipal_finance/municipalityprofilesrebuild/add/'
        )
        request.user = self.user
        obj = MunicipalityStaffContactsUpload()
        self.model_admin.save_model(
            obj=obj,
            request=request,
            form=None,
            change=None,
        )
        self.assertEquals(obj.user, self.user)
        record = OrmQ.objects.latest('id')
        self.assertEquals(
            record.func(),
            'municipal_finance.update.update_municipal_staff_contacts',
        )


class CashflowUpdateUploadTestCase(TransactionTestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_superuser(
            username='super',
            email='super@email.org',
            password='pass',
        )
        self.model_admin = CashflowUpdateAdmin(
            model=CashflowUpdate,
            admin_site=AdminSite(),
        )

    def test_save_task_trigger(self):
        request = self.factory.get(
            '/admin/municipal_finance/cashflowupdate/add/'
        )
        request.user = self.user
        obj = CashflowUpdate()
        self.model_admin.save_model(
            obj=obj,
            request=request,
            form=None,
            change=None,
        )
        self.assertEquals(obj.user, self.user)
        record = OrmQ.objects.latest('id')
        self.assertEquals(
            record.func(),
            'municipal_finance.update.update_cashflow',
        )
