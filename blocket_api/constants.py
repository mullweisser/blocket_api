from enum import IntEnum, StrEnum

SITE_URL = "https://www.blocket.se"
SEARCH_URL = f"{SITE_URL}/recommerce/forsale/search/api/search/SEARCH_ID_BAP_COMMON"
CAR_SEARCH_URL = f"{SITE_URL}/mobility/search/api/search/SEARCH_ID_CAR_USED"
BOAT_SEARCH_URL = f"{SITE_URL}/mobility/search/api/search/SEARCH_ID_BOAT_USED"
MC_SEARCH_URL = f"{SITE_URL}/mobility/search/api/search/SEARCH_ID_MC_USED"
ATV_SEARCH_URL = f"{SITE_URL}/mobility/search/api/search/SEARCH_ID_MC_ATV"
SNOWMOBILE_SEARCH_URL = f"{SITE_URL}/mobility/search/api/search/SEARCH_ID_MC_SNOWMOBILE"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"
}
