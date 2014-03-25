/login (POST)
/logout (GET)
/reset (POST)
/activate (POST)

Users Endpoints
/users/ (GET, POST)
/users/:id (GET,PATCH,DELETE)
/users/:id/demandAccounts/ (GET, POST) <-- Get = all demand accounts and the permissions for a user. POST = create a demandaccount for that user+perms
/users/:id/demandAccounts/:id (GET,POST,DELETE) <-- GET = that demand account. POST = creates/replaces relationship with that user and DA. DELETE = delete the relationship

DemandAccounts Endpoints
/demandAccounts/ (GET) <-- get all DAs I have access to (Maybe just return it as {data :DA})
/demandAccounts/:id (GET, PATCH, DELETE) <-- GET = get that DA. PATCH = update that DA. DELETE = delete that DA
/demandAccounts/:id/users/ (GET, POST) <-- GET = get all the users and their perms for the DA. POST = Creates or attaches a user(by username) for that demandAccount+perms 
/demandAccounts/:id/users/:id (GET, POST, DELETE) <-- GET = get User. POST = creates a relationship between user and DA . DELETE = Delete the relationship  
/demandAccounts/:id/campaigns (GET, POST)
/demandAccounts/:id/adUnits/ (GET, POST)
/demandAccounts/:id/postRolls/ (GET, POST)
/demandAccounts/:id/preRolls/ (GET, POST)
/demandAccounts/:id/videos/ (GET, POST) 
/demandAccounts/:id/geoGroups/ (GET, POST) 



/campaigns/:id (GET,PATCH,DELETE) Get the campaign, update the campaign, delete the campaign <-- Talk to Dan about Delete
/campaigns/:id/adGroups (GET, POST) GET = Get all the adgroups, POST = create a new adgroup on that campaign
/campaigns/:id/geoGroups (GET)
/campaigns/:id/geoGroups/:id (GET, POST, DELETE)
/campaigns/:id/platformVersions (GET)
/campaigns/:id/platformVersions/:id (GET,POST, DELETE)
/campaigns/:id/devices (GET)
/campaigns/:id/devices/:id (GET, POST, DELETE)
/campaigns/:id/connectionTypes (GET)
/campaigns/:id/connectionTypes/:id (GET, POST, DELETE)
/campaigns/:id/categories (GET)
/campaigns/:id/categories/:id (GET, POST, DELETE)
/campaigns/:id/languages (GET)
/campaigns/:id/languages/:id (GET, POST, DELETE)
/campaigns/:id/bidStrategy/ (GET)
/campaigns/:id/bidStrategy/:id (GET, POST, DELETE)
/campaigns/:id/rating/ (GET)
/campaigns/:id/rating/:id (GET, POST, DELETE)
/campaigns/:id/status/ (GET)
/campaigns/:id/status/:id (GET, POST, DELETE)


/adGroups/:id (GET,PATCH,DELETE) Get the adGroup, update the adGroup, delete the adGroup
/adGroups/:id/adUnits (GET) Get all the adUnits
/adGroups/:id/adUnits/:id (GET, DELETE) Gets the AdUnit, removes the adUnit from the adGroup
/adGroups/:id/adWindows/ (GET, POST) <-- Add to Jira
/adGroups/:id/adWindows/:id (GET) <-- delete from the top level endpoint? #TODO
/adGroups/:id/geoGroups/ (GET)
/adGroups/:id/geoGroups/:id (GET, POST, DELETE)
/adGroups/:id/platformVersions/ (GET)
/adGroups/:id/platformVersions/:id (GET, POST, DELETE)
/adGroups/:id/devices/ (GET)
/adGroups/:id/devices/:id (GET, POST, DELETE)
/adGroups/:id/connectionTypes/ (GET)
/adGroups/:id/connectionTypes/:id (GET, POST, DELETE)
/adGroups/:id/categories/ (GET)
/adGroups/:id/categories/:id (GET, POST, DELETE)
/adGroups/:id/ISULists/ (GET)
/adGroups/:id/ISULists/:id (GET, POST, DELETE)
/adGroups/:id/siteIDLists/ (GET)
/adGroups/:id/siteIDLists/:id (GET, POST, DELETE)
/adGroups/:id/status (GET)
/adGroups/:id/status/:id (GET, POST, DELETE)
/adGroups/:id/rating (GET)
/adGroups/:id/rating/:id (GET, POST, DELETE)
/adGroups/:id/language (GET)
/adGroups/:id/language/:id (GET, POST, DELETE)


/adUnits/:id (GET, PATCH, DELETE)
/adUnits/:id/adGroups/ (GET)
/adUnits/:id/video/ (GET)
/adUnits/:id/video/:id  (GET, POST, DELETE)
/adUnits/:id/preRoll/ (GET)
/adUnits/:id/preRoll/:id (GET, POST, DELETE)
/adUnits/:id/postRoll/ (GET)
/adUnits/:id/postRoll/:id (GET, POST, DELETE)
/adUnits/:id/status (GET)
/adUnits/:id/status/:id (GET, POST, DELETE)
/adUnits/:id/rating (GET)
/adUnits/:id/rating/:id (GET, POST, DELETE)
/adUnits/:id/language (GET)
/adUnits/:id/language/:id (GET, POST, DELETE)
/adUnits/:id/category (GET)
/adUnits/:id/category/:id (GET, POST, DELETE)
/adUnits/:id/metaTags/ (GET)
/adUnits/:id/metaTags/:id (GET, POST, DELETE)
/adUnits/:id/tpat/ (GET) #TODO
/adUnits/:id/tpat/:id (GET, POST, DELETE) #TODO


/bidStrategies/ (GET, POST)
/bidStrategies/:id (GET, PATCH, DELETE)

/categories/ (GET, POST)
/categories/:id (GET, PATCH, DELETE)

/companies/ (GET, POST)
/companies/:id (GET, PATCH, DELETE)

/connectionTypes/ (GET, POST)
/connectionTypes/:id (GET, PATCH, DELETE)

/devices/ (GET, POST)
/devices/:id (GET, PATCH, DELETE)

/languages/ (GET, POST)
/languages/:id (GET, PATCH, DELETE)

/metaTags/ (GET, POST)
/metaTags/:id (GET, PATCH, DELETE)

/oems/ (GET, POST)
/oems/:id (GET, PATCH, DELETE)

/platforms/ (GET, POST)
/platforms/:id (GET, PATCH, DELETE)

/platformVersions/ (GET, POST)
/platformVersions/:id (GET, PATCH, DELETE)

/ratings/ (GET, POST)
/ratings/:id (GET, PATCH, DELETE)

/status/ (GET, POST)
/status/:id (GET, PATCH, DELETE)

