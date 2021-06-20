from future.utils import with_metaclass
from ia32_python.utils.ia32_struct import *
from ia32_python.utils.ia32_bit_field import *


__doc__ = """
@brief Natural-Width Guest-State Fields

Natural-Width Guest-State Fields.
"""


VMCS_GUEST_CR0 = 0x6800


VMCS_GUEST_CR3 = 0x6802


VMCS_GUEST_CR4 = 0x6804


VMCS_GUEST_ES_BASE = 0x6806


VMCS_GUEST_CS_BASE = 0x6808


VMCS_GUEST_SS_BASE = 0x680a


VMCS_GUEST_DS_BASE = 0x680c


VMCS_GUEST_FS_BASE = 0x680e


VMCS_GUEST_GS_BASE = 0x6810


VMCS_GUEST_LDTR_BASE = 0x6812


VMCS_GUEST_TR_BASE = 0x6814


VMCS_GUEST_GDTR_BASE = 0x6816


VMCS_GUEST_IDTR_BASE = 0x6818


VMCS_GUEST_DR7 = 0x681a


VMCS_GUEST_RSP = 0x681c


VMCS_GUEST_RIP = 0x681e


VMCS_GUEST_RFLAGS = 0x6820


VMCS_GUEST_PENDING_DEBUG_EXCEPTIONS = 0x6822


VMCS_GUEST_SYSENTER_ESP = 0x6824


VMCS_GUEST_SYSENTER_EIP = 0x6826


VMCS_GUEST_S_CET = 0x6c28


VMCS_GUEST_SSP = 0x6c2a


VMCS_GUEST_INTERRUPT_SSP_TABLE_ADDR = 0x6c2c


