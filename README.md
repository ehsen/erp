# ERP
A full blown ERP with automatic compliance with IFRS and Tax authorities. 

# Why another ERP
I am starting this project out of frustration with current ERPs and accounting softwares. Becuase they are just doing high school accounting or requires highly expensive customization. Plus have you ever try to explain IFRS 9 to a programmer? Good Luck with that.

Being an accountant, at the end I am the one who is preparing all returns for tax authorities, ensuring compliance with IFRS. ERPs are presenting me with fancy graphs and dashboards which in most cases are useless, at least for me. Businesses dont pay me for fancy graphs. 

# About Architecture
ERPs are inherently complex software however I ll try to implement it in a simple, straightforward way. Everything is a MongoDB document in our ERP which will go through
a workflow. The core of the ERP is the accounting transaction, whethere we are moving items from one warehouse to another, doing process accounting or something else.
Performing majority of the ERP operations with simple DEBITS and CREDITS will streamline the whole operation rather than doing kung fu with complicated architectures.

This area is still work in progress.... So I may change things here

# Current Progress
Currently I am working on  account types and their interaction with IFRS and Tax Codes.





