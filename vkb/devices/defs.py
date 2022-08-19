from .base import VENDOR_ID
from .gladiatork import GladiatorK, NXT_SEM_THQ_FSMGA, GladiatorK_THQ

VKB_DEVICES = {0x0132: GladiatorK, 0x2234: NXT_SEM_THQ_FSMGA, 0x0210: GladiatorK_THQ}
