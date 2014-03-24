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
/demandAccounts/:id/users/ (GET, POST) <-- GET = get all the users and their perms for the DA. POST = Creates a user for that demandAccount+perms 
/demandAccounts/:id/users/:id (GET, POST, DELETE) <-- GET = get User. POST = creates a relationship between user and DA . DELETE = Delete the relationship  
/demandAccounts/:id/campaigns (GET, POST)
/demandAccounts/:id/adUnits/ (GET, POST)
/demandAccounts/:id/postRolls/ (GET, POST)
/demandAccounts/:id/preRolls/ (GET, POST)
/demandAccounts/:id/videos/ (GET, POST) 
/demandAccounts/:id/geoGroups/ (GET, POST) 



/campaigns/:id (GET,PATCH,DELETE) Get the campaign, update the campaign, delete the campaign <-- Talk to Dan about Delete
/campaigns/:id/adGroups (GET, POST) GET = Get all the adgroups, POST = create a new adgroup on that campaign
/campaigns/:id/adGroups/:id (GET) Get the adgroup
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


/adGroups/:id
/adGroups/:id/adUnits
/adGroups/:id/adUnits/:id


/adUnits/
/adUnits/:id
/adUnits/:id/video/:id
/adUnits/:id/preRoll/:id
/adUnits/:id/postRoll/:id

/connectionTypes/ (GET, POST(admin only)))
/connectionTypes/:id (GET, PATCH(admin only), DELETE(admin only))


