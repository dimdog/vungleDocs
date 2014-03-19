/login
/logout
/reset_password
/TODO -first time log in

/users/ (GET, POST)
/users/:id (GET,PATCH,DELETE)
/users/:id/demandAccounts/ (GET, POST)
/users/:id/demandAccounts/:id (GET,POST,DELETE)

/demandAccounts/ (GET)
/demandAccounts/:id (GET, DELETE)
/demandAccounts/:id/users/ (GET, PATCH, POST, DELETE) 
/demandAccounts/:id/campaigns (GET, POST)
/demandAccounts/:id/adUnits/ (GET, POST)
/demandAccounts/:id/postRolls/ (GET, POST)
/demandAccounts/:id/preRolls/ (GET, POST)
/demandAccounts/:id/videos/ (GET, POST) 


/campaigns/
/campaigns/:id
/campaigns/:id/adGroups
/campaigns/:id/adGroups/:id
/campaigns/:id/geoGroups
/campaigns/:id/geoGroups/:id
/campaigns/:id/platformVersions
/campaigns/:id/platformVersions/:id
/campaigns/:id/devices
/campaigns/:id/devices/:id
/campaigns/:id/connectionTypes
/campaigns/:id/connectionTypes/:id
/campaigns/:id/categories
/campaigns/:id/categories/:id
/campaigns/:id/languages
/campaigns/:id/languages/:id
/campaigns/:id/bidStrategy/:id
/campaigns/:id/rating/:id
/campaigns/:id/status/:id <-- ??TODO
/campaigns/:id/demandAccount/:id <-- ??????TODO


/adGroups/
/adGroups/:id
/adGroups/:id/adUnits
/adGroups/:id/adUnits/:id


/adUnits/
/adUnits/:id
/adUnits/:id/video/:id
/adUnits/:id/preRoll/:id
/adUnits/:id/postRoll/:id




