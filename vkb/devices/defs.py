from .base import VENDOR_ID
from .gladiatork import GladiatorK, NXT_SEM_THQ_FSMGA, GladiatorK_THQ, NXT_SEM_2xTHQ_FSMGA, GladiatorNXT_SCG_PL

VKB_DEVICES = {0x2224: NXT_SEM_2xTHQ_FSMGA, 0x2234: NXT_SEM_THQ_FSMGA, 0x0132: GladiatorK, 0x0210: GladiatorK_THQ, 0x0201: GladiatorNXT_SCG_PL}
