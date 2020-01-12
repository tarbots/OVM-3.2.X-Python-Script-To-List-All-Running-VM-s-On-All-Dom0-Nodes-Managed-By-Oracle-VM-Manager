# ====================================================================
#  Script prints VirtServerCurrentState of vServers in format:
#
#    <OVM_UUID>|<status>|<UFN>|<CN>
#
#    where: 
#      OVM_UUID - is OVM's UUID of VM 
#      status   - is state of vServer, it can have values:
#                    Running
#                    Starting
#                    Stopped
#                    Stopping
#                    Suspended
#                    None
#      UFN      - User Friendly Name of VM
#      CN       - OVS Node to which is vServer associated
#         
#      
# ====================================================================

from com.oracle.ovm.mgr.api.event import PowerEvent,StatusEvent
from com.oracle.ovm.mgr.api import OvmClient
from com.oracle.ovm.mgr.api.virtual import VirtualMachine 

print "\n".join([ "%s|%s|%s|%s" %(i.getName(), i.getStatusEvent(PowerEvent, StatusEvent.Severity.INFORMATIONAL).getStatus(), i.getSimpleName(), i.getServer()) for i in OvmClient.getOvmManager().getObjects(VirtualMachine)])
