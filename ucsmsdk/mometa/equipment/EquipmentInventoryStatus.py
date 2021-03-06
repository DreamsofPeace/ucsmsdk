"""This module contains the general information for EquipmentInventoryStatus ManagedObject."""

from ...ucsmo import ManagedObject
from ...ucscoremeta import MoPropertyMeta, MoMeta
from ...ucsmeta import VersionMeta


class EquipmentInventoryStatusConsts:
    CLEANUP_PARENT_ON_DISCOVERY_FALSE = "false"
    CLEANUP_PARENT_ON_DISCOVERY_NO = "no"
    CLEANUP_PARENT_ON_DISCOVERY_TRUE = "true"
    CLEANUP_PARENT_ON_DISCOVERY_YES = "yes"


class EquipmentInventoryStatus(ManagedObject):
    """This is EquipmentInventoryStatus class."""

    consts = EquipmentInventoryStatusConsts()
    naming_props = set([])

    mo_meta = MoMeta("EquipmentInventoryStatus", "equipmentInventoryStatus", "inv-status", None, "InputOutput", 0x3f, [], ["read-only"], [u'adaptorUnit', u'adaptorUnitExtn', u'computeBlade', u'computeRackUnit', u'computeServerUnit', u'graphicsCard', u'memoryUnit', u'processorUnit', u'securityUnit', u'storageController'], [u'faultInst'], [None])

    prop_meta = {
        "child_action": MoPropertyMeta("child_action", "childAction", "string", None, MoPropertyMeta.INTERNAL, 0x2, None, None, r"""((deleteAll|ignore|deleteNonPresent),){0,2}(deleteAll|ignore|deleteNonPresent){0,1}""", [], []), 
        "cleanup_parent_on_discovery": MoPropertyMeta("cleanup_parent_on_discovery", "cleanupParentOnDiscovery", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, None, ["false", "no", "true", "yes"], []), 
        "dn": MoPropertyMeta("dn", "dn", "string", None, MoPropertyMeta.READ_ONLY, 0x4, 0, 256, None, [], []), 
        "hw_inventory_status": MoPropertyMeta("hw_inventory_status", "hwInventoryStatus", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""((defaultValue|ok|pci-config-mismatch|mismatch|insertion|removal|replacement),){0,6}(defaultValue|ok|pci-config-mismatch|mismatch|insertion|removal|replacement){0,1}""", [], []), 
        "id": MoPropertyMeta("id", "id", "uint", None, MoPropertyMeta.READ_WRITE, 0x8, None, None, None, [], []), 
        "model": MoPropertyMeta("model", "model", "string", None, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "revision": MoPropertyMeta("revision", "revision", "string", None, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "rn": MoPropertyMeta("rn", "rn", "string", None, MoPropertyMeta.READ_ONLY, 0x10, 0, 256, None, [], []), 
        "sacl": MoPropertyMeta("sacl", "sacl", "string", None, MoPropertyMeta.READ_ONLY, None, None, None, r"""((none|del|mod|addchild|cascade),){0,4}(none|del|mod|addchild|cascade){0,1}""", [], []), 
        "serial": MoPropertyMeta("serial", "serial", "string", None, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
        "status": MoPropertyMeta("status", "status", "string", None, MoPropertyMeta.READ_WRITE, 0x20, None, None, r"""((removed|created|modified|deleted),){0,3}(removed|created|modified|deleted){0,1}""", [], []), 
        "vendor": MoPropertyMeta("vendor", "vendor", "string", None, MoPropertyMeta.READ_ONLY, None, 0, 510, None, [], []), 
    }

    prop_map = {
        "childAction": "child_action", 
        "cleanupParentOnDiscovery": "cleanup_parent_on_discovery", 
        "dn": "dn", 
        "hwInventoryStatus": "hw_inventory_status", 
        "id": "id", 
        "model": "model", 
        "revision": "revision", 
        "rn": "rn", 
        "sacl": "sacl", 
        "serial": "serial", 
        "status": "status", 
        "vendor": "vendor", 
    }

    def __init__(self, parent_mo_or_dn, **kwargs):
        self._dirty_mask = 0
        self.child_action = None
        self.cleanup_parent_on_discovery = None
        self.hw_inventory_status = None
        self.id = None
        self.model = None
        self.revision = None
        self.sacl = None
        self.serial = None
        self.status = None
        self.vendor = None

        ManagedObject.__init__(self, "EquipmentInventoryStatus", parent_mo_or_dn, **kwargs)
