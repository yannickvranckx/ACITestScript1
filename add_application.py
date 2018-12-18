#!/usr/bin/env python


# list of packages that should be imported for this code to work
import cobra.mit.access
import cobra.mit.request
import cobra.mit.session
import cobra.model.fv
import cobra.model.pol
from cobra.internal.codec.xmlcodec import toXMLStr
from credentials import *


# configuration variables
tenant = 'Downfall'
bridge_domain = 'Downfallland'
application = 'Save_the_wild'
vlan1 = 'vlan-211'
vlan2 = 'vlan-212'
vlan3 = 'vlan-210'


# log into an APIC and create a directory object
ls = cobra.mit.session.LoginSession(URL, LOGIN, PASSWORD)
md = cobra.mit.access.MoDirectory(ls)
md.login()

# the top level object on which operations will be made
polUni = cobra.model.pol.Uni('')
fvTenant = cobra.model.fv.Tenant(polUni, tenant)


## the Application name "Save_The_Planet" should be changed to the application variable
fvAp = cobra.model.fv.Ap(fvTenant, ownerKey=u'', name=application, prio=u'unspecified', ownerTag=u'', descr=u'')

# create the first EPG underneath your new Application.
fvAEPg = cobra.model.fv.AEPg(fvAp, isAttrBasedEPg=u'no', matchT=u'AtleastOne', prio=u'unspecified', name=u'app', descr=u'')

# have the EPG created by the previous line of code consume the "sql" contract.
fvRsCons = cobra.model.fv.RsCons(fvAEPg, tnVzBrCPName=u'sql', prio=u'unspecified')

# assign a VLAN and vPC to the EPG represented by fvAEPg
## the encap should be changed to use the vlan1 variable
fvRsPathAtt = cobra.model.fv.RsPathAtt(fvAEPg, tDn=u'topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]', instrImedcy=u'lazy', encap=vlan1, descr=u'', mode=u'regular')

# assign a VLAN and a second vPC to the EPG represented by fvAEPg
## the encap should be changed to use the vlan1 variable
fvRsPathAtt2 = cobra.model.fv.RsPathAtt(fvAEPg, tDn=u'topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2A]', instrImedcy=u'lazy', encap=vlan1, descr=u'', mode=u'regular')

# creates a relationship between the EPG represented by fvAEPg and a Physical Domain.
# this determines what encapsulation values can be used.
fvRsDomAtt = cobra.model.fv.RsDomAtt(fvAEPg, instrImedcy=u'lazy', resImedcy=u'lazy', encap=u'unknown', tDn=u'uni/phys-Heroes_phys')

# sets the QoS policy for the EPG represented by fvAEPg
fvRsCustQosPol = cobra.model.fv.RsCustQosPol(fvAEPg, tnQosCustomPolName=u'')

# this assigns the Bridge Domain that hosts in fvAEPg will belong to. the Bridge
# Domain provides a flooding domain and a set of subnets the hosts can belong to.
## the Bridge Domain name should be changed from "Hero_Land" to the bridge_domain variable
fvRsBd = cobra.model.fv.RsBd(fvAEPg, tnFvBDName=bridge_domain)

# have the EPG represented by the fvAEPg object provide the "power_up" contract
fvRsProv = cobra.model.fv.RsProv(fvAEPg, tnVzBrCPName=u'power_up', matchT=u'AtleastOne', prio=u'unspecified')

# creates a new EPG object represented by the name fvAEPg2
fvAEPg2 = cobra.model.fv.AEPg(fvAp, isAttrBasedEPg=u'no', matchT=u'AtleastOne', prio=u'unspecified', name=u'db', descr=u'')

# assign a VLAN and vPC to the EPG represented by fvAEPg2
## the encap should be changed to use the vlan2 variable
fvRsPathAtt3 = cobra.model.fv.RsPathAtt(fvAEPg2, tDn=u'topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]', instrImedcy=u'lazy', encap=vlan2, descr=u'', mode=u'regular')

# assign a VLAN and a second vPC to the EPG represented by fvAEPg2
## the encap should be changed to use the vlan2 variable"
fvRsPathAtt4 = cobra.model.fv.RsPathAtt(fvAEPg2, tDn=u'topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2A]', instrImedcy=u'lazy', encap=vlan2, descr=u'', mode=u'regular')

# creates a relationship between the EPG represented by fvAEPg2 and a Physical Domain.
fvRsDomAtt2 = cobra.model.fv.RsDomAtt(fvAEPg2, instrImedcy=u'lazy', resImedcy=u'lazy', encap=u'unknown', tDn=u'uni/phys-Heroes_phys')

# sets the QoS policy for the EPG represented by fvAEPg2
fvRsCustQosPol2 = cobra.model.fv.RsCustQosPol(fvAEPg2, tnQosCustomPolName=u'')

# this assigns the Bridge Domain that hosts in the fvAEPg2 will belong to
## the Bridge Domain name should be changed from "Hero_Land" to the bridge_domain variable
fvRsBd2 = cobra.model.fv.RsBd(fvAEPg2, tnFvBDName=bridge_domain)

# have the EPG represented by the fvAEPg2 object provide the "sql" contract
fvRsProv2 = cobra.model.fv.RsProv(fvAEPg2, tnVzBrCPName=u'sql', matchT=u'AtleastOne', prio=u'unspecified')

# creates a new EPG object represented by the name fvAEPg3
fvAEPg3 = cobra.model.fv.AEPg(fvAp, isAttrBasedEPg=u'no', matchT=u'AtleastOne', prio=u'unspecified', name=u'web', descr=u'')

# have the EPG created by the previous line of code consume the "sql" contract.
fvRsCons2 = cobra.model.fv.RsCons(fvAEPg3, tnVzBrCPName=u'sql', prio=u'unspecified')

# assign a VLAN and vPC to the EPG represented by fvAEPg3
## the encap should be changed to use the vlan3 variable
fvRsPathAtt5 = cobra.model.fv.RsPathAtt(fvAEPg3, tDn=u'topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2B]', instrImedcy=u'lazy', encap=vlan3, descr=u'', mode=u'regular')

# assign a VLAN and a second vPC to the EPG represented by fvAEPg3
## the encap should be changed to use the vlan3 variable
fvRsPathAtt6 = cobra.model.fv.RsPathAtt(fvAEPg3, tDn=u'topology/pod-1/protpaths-101-102/pathep-[Heroes_FI-2A]', instrImedcy=u'lazy', encap=vlan3, descr=u'', mode=u'regular')

# creates a relationship between the EPG represented by fvAEPg3 and a Physical Domain.
fvRsDomAtt3 = cobra.model.fv.RsDomAtt(fvAEPg3, instrImedcy=u'lazy', resImedcy=u'lazy', encap=u'unknown', tDn=u'uni/phys-Heroes_phys')

# sets the QoS policy for the EPG represented by fvAEPg3
fvRsCustQosPol3 = cobra.model.fv.RsCustQosPol(fvAEPg3, tnQosCustomPolName=u'')

# this assigns the Bridge Domain that hosts in the fvAEPg3 will belong to
## the Bridge Domain name should be changed from "Hero_Land" to the bridge_domain variable
fvRsBd3 = cobra.model.fv.RsBd(fvAEPg3, tnFvBDName=bridge_domain)

# have the EPG represented by the fvAEPg3 object provide the "web" contract
fvRsProv3 = cobra.model.fv.RsProv(fvAEPg3, tnVzBrCPName=u'web', matchT=u'AtleastOne', prio=u'unspecified')

# commit the generated code to APIC
print toXMLStr(fvTenant)
c = cobra.mit.request.ConfigRequest()
c.addMo(fvTenant)
md.commit(c)