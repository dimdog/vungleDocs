/login
/logout
/reset_password
/TODO -first time log in

/users/ (GET, POST)
/users/:id (GET,PATCH,DELETE)
/users/:id/demandAccounts/ (GET)
/users/:id/demandAccounts/:id (GET,POST,PATCH,DELETE)


/demandAccounts/
/demandAccounts/:id
/demandAccounts/:id/campaigns
/demandAccounts/:id/adUnits/
/demandAccounts/:id/users/ <--Chopping block?
/demandAccounts/:id/postRolls/
/demandAccounts/:id/postRolls/:id
/demandAccounts/:id/preRolls/
/demandAccounts/:id/preRolls/:id
/demandAccounts/:id/videos/
/demandAccounts/:id/videos/:id


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




