from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkdns.v2 import DnsClient, UpdateRecordSetRequest, UpdateRecordSetReq
from huaweicloudsdkdns.v2.region.dns_region import DnsRegion
from loguru import logger

from ddns.settings import settings


def huawei_ddns(ip: str):
    credentials = BasicCredentials(settings.cloud_sdk_ak, settings.cloud_sdk_sk)
    client = DnsClient.new_builder().with_credentials(credentials).with_region(DnsRegion.value_of("cn-east-3")).build()

    try:
        request = UpdateRecordSetRequest()
        request.zone_id = settings.zone_id
        request.recordset_id = settings.recordset_id

        request.body = UpdateRecordSetReq(
            records=[ip],
            type="A",
            name=settings.name
        )
        response = client.update_record_set(request)
        logger.info(response)
    except Exception as e:
        logger.exception(e)
