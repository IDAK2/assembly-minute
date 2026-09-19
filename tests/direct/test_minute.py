from conftest import CONTRACT
def test_publish_and_object(direct_vm,direct_deploy,direct_alice,direct_bob):
 direct_vm.sender=direct_alice;x=direct_deploy(CONTRACT);x.open_motion('m-1','0x'+direct_bob.hex(),'Adopt the watershed maintenance budget.');x.adopt('m-1','Passed 8–2',['North ward reserved on timing'],'Treasurer');direct_vm.mock_web(r'minutes\.example',{'status':200,'body':'Motion adopted 8-2. North ward timing reservation. Treasurer owns action.'});direct_vm.mock_llm(r'.*AssemblyMinute fidelity check.*','{"faithful":true}');x.publish('m-1','https://minutes.example/m1');x.object_minute('m-1','https://member.example/objection');assert x.get_minute('m-1')['state']=='OBJECTED';direct_vm.sender=direct_bob;x.reconcile('m-1','https://minutes.example/m1-corrected');assert x.get_minute('m-1')['state']=='RECONCILED'
def test_reviewer_separate(direct_vm,direct_deploy,direct_alice):
 direct_vm.sender=direct_alice
 with direct_vm.expect_revert('independent reviewer'):direct_deploy(CONTRACT).open_motion('m-1','0x'+direct_alice.hex(),'A sufficiently substantive motion.')
