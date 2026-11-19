"""Curated geographic parent paths for exact place labels in lecture metadata.

Only explicit, stable geographic associations belong here. The leaf is preserved
verbatim for search/backward compatibility; these paths do not imply modern
nationality, historical sovereignty, or that all places in a region are covered.

Ambiguous labels (for example Cambridge and Plains) must instead be resolved in
an individual lecture's authored ``tag_paths`` after checking its context.
Oceanic, polar, Indigenous, and transborder places are not forced into a country.
"""

# Parent groups are explicit editorial classifications of the labels below.
# The reader prepends "Place: " to every element in a geographic path.
_GROUPS = [
    # Europe: modern names locate a place, not the allegiance of historic people.
    (('Europe', 'Britain', 'Scotland'), (
        'Aberdeen', 'Edinburgh', 'Edinburgh, Scotland', 'Glasgow, Scotland',
        'Glenlair', 'Scottish Highlands, Scotland, United Kingdom',
        'Scottish Highlands, United Kingdom', 'Siccar Point, Scottish Borders, Scotland, United Kingdom',
    )),
    (('Europe', 'Britain', 'England'), (
        'Cambridge, England', 'England, United Kingdom', 'Bletchley Park, England',
        'Kingston upon Thames', 'Lincoln, England', 'London, England',
        'London, England, United Kingdom', 'Manchester, England',
        'Newington Butts', 'Oxford, England', 'Shrewsbury, England',
        'Southampton, England', 'Woolsthorpe, Lincolnshire, England',
        'Royal Institution, London', 'Down House, Kent', 'Down, Kent',
    )),
    (('Europe', 'Britain'), ('Northern Ireland',)),
    (('Europe', 'Ireland'), ('Cork, Ireland',)),
    (('Europe', 'France'), (
        'Arbois, Jura', 'Bourg-la-Reine, France', 'Bures-sur-Yvette',
        'Cherbourg, France', 'Clermont-Ferrand, France', 'Dijon, France',
        'Dole, Jura', 'Lille', 'Montpellier, France', 'Paris, France',
        'Pouilly-le-Fort, Seine-et-Marne', 'Rouen, France', 'Strasbourg',
    )),
    (('Europe', 'France', 'Paris'), ('Arsenal district, Paris',)),
    (('Europe', 'Germany'), (
        'Berlin, Germany', 'Bonn', 'Brunswick (Braunschweig), Germany',
        'Erlangen, Germany', 'Freiberg, Saxony', 'Freiburg im Breisgau',
        'Göttingen, Germany', 'Hamburg, Germany', 'Hanover, Germany',
        'Heidelberg', 'Heidelberg, Germany', 'Karlsruhe', 'Karlsruhe, Germany',
        'Leipzig, Germany', 'Marburg, Germany', 'Regensburg, Germany',
        'Tübingen, Germany', 'Ulm, Germany',
    )),
    (('Europe', 'Germany', 'Berlin'), ('Berlin-Dahlem',)),
    (('Europe', 'Central Europe'), ('Württemberg',)),
    (('Europe', 'Switzerland'), ('Basel, Switzerland', 'Bern, Switzerland')),
    (('Europe', 'Austria'), ('Graz, Austria', 'Linz, Austria', 'Vienna, Austria')),
    (('Europe', 'Poland'), ('Kraków, Poland', 'Warsaw, Poland', 'Wrocław',
                          'Breslau (now Wrocław, Poland)')),
    (('Europe', 'Central Europe', 'Silesia'), ('Breslau',)),
    (('Europe', 'Hungary'), ('Budapest, Hungary', 'Buda and Pest (now Budapest), Hungary')),
    (('Europe', 'Czechia'), ('Brno (Brünn)', 'Prague', 'Prague, Czechia')),
    (('Europe', 'Spain'), ('Barcelona, Spain', 'Madrid, Spain', 'La Coruña')),
    (('Europe', 'Italy'), (
        'Bologna', 'Brescia', 'Gallarate', 'Milan', 'Pavia', 'Padua',
        'Saccolongo', 'Verona', 'Turin, Italy', 'Lake Maggiore, Italy',
    )),
    (('Europe', 'Belgium'), ('Ypres, Belgium',)),
    (('Europe', 'Denmark'), ('Copenhagen, Denmark',)),
    (('Europe', 'Netherlands'), ('Delft, Netherlands',)),
    (('Europe', 'Northern Europe', 'Sweden'), (
        'Hven (Ven), Sweden', 'Scania (then Denmark; now Sweden)',
        'Stockholm', 'Stockholm, Sweden',
    )),
    (('Europe', 'Northern Europe', 'Norway'), ('Oslo',)),
    (('Europe', 'Northern Europe'), ('Norway',)),
    (('Europe', 'Iceland'), ('Eyjafjallajökull, Iceland',)),
    (('Europe', 'Eastern Europe', 'Ukraine'), ('Lwów (now Lviv, Ukraine)', 'Odessa')),
    # Russia spans continents; locating a city is not attributing nationality.
    (('Eurasia', 'Russia'), (
        'Moscow, Russia', 'Saint Petersburg (Petrograd/Leningrad), Russia',
        'Saint Petersburg, Russia', 'Leningrad (Saint Petersburg)',
        'Saratov, Russia', 'Tobolsk',
    )),
    (('Eurasia', 'Ural Mountains'), ('Urals',)),

    (('Europe', 'Germany', 'Hanover'), ('Breselenz, Hanover',)),
    (('Europe', 'Britain', 'England'), ('Shrewsbury',)),
    (('Europe', 'Romania'), ('Bucharest',)),

    # Americas, including North American historical regions and border-spanning places.
    (('Americas', 'North America'), (
        'British North America', 'Haudenosaunee homelands', 'Pacific Northwest, North America',
        'Ohio Country', 'Ohio River Valley', 'Great Plains, United States',
        'Appalachian Mountains, eastern United States', 'Blue Ridge, eastern United States',
        'Southern United States', 'Northwest Territory',
    )),
    (('Americas', 'North America', 'United States'), (
        'New York, United States', 'California, United States',
        'Hawaii, United States', 'New Mexico, United States',
        'Texas, United States', 'Washington, United States',
        'Michigan, United States', 'Alaska, United States',
        'Oregon, United States',
    )),
    (('Americas', 'North America', 'United States'), (
        'Indiana', 'Kansas', 'Maine', 'Maryland', 'Mississippi', 'Missouri',
        'South Carolina', 'Tennessee', 'Texas', 'Virginia',
        'New Mexico',
        'High Plains Aquifer, United States',
        'Arizona and New Mexico, United States',
        'Palisades, New Jersey and New York, United States',
    )),
    (('Americas', 'North America', 'United States', 'Arizona'), (
        'San Pedro River near Tombstone, Arizona, United States',
        # Julia Robinson's childhood in the Phoenix area; see 165000 source timeline.
        'Near Camelback Mountain',
    )),
    (('Americas', 'North America', 'United States', 'California'), (
        'Año Nuevo, California, United States', 'Los Angeles, California, United States',
        'Montecito, California, United States', 'Newport Beach, California, United States',
        'Northern California, United States', 'Lake Oroville, California, United States',
        'Pasadena, California', 'Palomar Observatory, California',
        'San Diego', 'San Diego, California', 'San Francisco, California, United States',
        'San Joaquin Valley, California, United States',
        'Santa Monica', 'Santa Monica, California, United States',
        'Santa Ynez Mountains, California, United States',
        'Sierra Nevada, California, United States', 'Ventura, California, United States',
        'Yosemite, California, United States', 'Stanford, California',
        'Point Loma', 'Pebble Beach',
    )),
    (('Americas', 'North America', 'United States', 'Connecticut'), (
        'Hartford, Connecticut', 'New Haven, Connecticut',
    )),
    (('Americas', 'North America', 'United States', 'Georgia'), ('Atlanta',)),
    (('Americas', 'North America', 'United States', 'Illinois'), (
        'Chicago, Illinois, United States',
    )),
    (('Americas', 'North America', 'United States', 'Louisiana'), (
        'Atchafalaya River, Louisiana, United States',
        'Breton Sound, Louisiana, United States',
        'Mississippi River Delta, Louisiana, United States',
    )),
    (('Americas', 'North America', 'United States', 'Maine'), (
        'Boothbay Harbor', 'Southport Island',
    )),
    (('Americas', 'North America', 'United States', 'Maryland'), (
        'Annapolis', 'Silver Spring', 'Silver Spring, Maryland',
    )),
    (('Americas', 'North America', 'United States', 'Massachusetts'), (
        'Cambridge, Massachusetts', 'Cambridge, Massachusetts, United States',
        'Duxbury', 'Quashnet River, Cape Cod, Massachusetts, United States',
        'Woods Hole',
    )),
    (('Americas', 'North America', 'United States', 'Michigan'), ('Ypsilanti, Michigan, United States',)),
    (('Americas', 'North America', 'United States', 'Mississippi'), ('Vicksburg',)),
    (('Americas', 'North America', 'United States', 'Missouri'), (
        'Columbia, Missouri', 'St. Louis',
    )),
    (('Americas', 'North America', 'United States', 'Montana'), ('Glacier National Park, Montana, United States',)),
    (('Americas', 'North America', 'United States', 'New Jersey'), (
        'Island Beach, New Jersey, United States',
        'Mantoloking, New Jersey, United States',
        'Princeton (New Jersey)',
    )),
    (('Americas', 'North America', 'United States', 'New Mexico'), (
        'Los Alamos, New Mexico', 'Trinity Site, New Mexico',
    )),
    (('Americas', 'North America', 'United States', 'New York'), (
        'Brooklyn, New York', 'Catskills, New York, United States',
        'Cold Spring Harbor, New York', 'Hudson River estuary, New York, United States',
        'Ithaca, New York', 'Jones Beach Island, New York, United States',
        'New York City, United States',
        'Long Island', 'Long Island, New York, United States',
        'Poughkeepsie, New York', 'Rockaway Peninsula, New York, United States',
        'Stony Brook, New York',
    )),
    (('Americas', 'North America', 'United States', 'North Carolina'), (
        'Durham, North Carolina', 'North Core Banks, North Carolina, United States',
        'Pamlico Sound, North Carolina, United States',
    )),
    (('Americas', 'North America', 'United States', 'Ohio'), ('Toledo, Ohio, United States',)),
    (('Americas', 'North America', 'United States', 'Oregon'), (
        'Portland, Oregon', 'Eugene',
    )),
    (('Americas', 'North America', 'United States', 'Pennsylvania'), (
        'Bryn Mawr, Pennsylvania', 'Gettysburg', 'Pennsylvania oil region',
        'Philadelphia', 'Philadelphia, Pennsylvania, United States',
        'Pittsburgh', 'Springdale', 'Springdale, Pennsylvania',
    )),
    (('Americas', 'North America', 'United States', 'Tennessee'), (
        'Chattanooga', 'Fort Donelson', 'Shiloh',
    )),
    (('Americas', 'North America', 'United States', 'Texas'), (
        'Comal and San Marcos Springs, central Texas, United States',
        'Edwards Aquifer, central Texas, United States',
        'Southeastern Texas, United States',
    )),
    (('Americas', 'North America', 'United States', 'Virginia'), (
        'Arlington, Virginia', 'Manassas', 'Mount Vernon',
    )),
    (('Americas', 'North America', 'United States', 'Washington'), (
        'Mount Rainier, Washington, United States',
        'Mount St. Helens, Washington, United States',
        'North Fork Stillaguamish River, Washington, United States',
        'Oso, Washington, United States', 'Puyallup River, Washington, United States',
    )),
    (('Americas', 'North America', 'United States', 'Wisconsin'), (
        'Williams Bay, Wisconsin, United States',
    )),
    (('Americas', 'North America', 'United States', 'Hawaii'), ('Mauna Loa, Hawaii, United States',)),
    (('Americas', 'North America', 'United States', 'Wyoming'), (
        'Yellowstone, Wyoming, United States',
    )),
    (('Americas', 'North America', 'United States', 'Washington, D.C.'), (
        'Washington DC',
    )),
    (('Americas', 'North America', 'United States', 'Chesapeake Bay'), (
        'Chesapeake Bay, Maryland and Virginia, United States',
    )),
    (('Americas', 'North America', 'Canada'), (
        'British Columbia, Canada', 'Newfoundland, Canada',
    )),
    (('Americas', 'North America', 'Canada', 'British Columbia'), (
        'Lytton, British Columbia, Canada',
    )),
    (('Americas', 'North America', 'Canada', 'Ontario'), (
        'Experimental Lakes Area, Ontario, Canada',
    )),
    (('Americas', 'North America', 'Canada', 'Nova Scotia'), (
        'Minas Basin, Nova Scotia, Canada',
    )),
    (('Americas', 'North America', 'Canada', 'Quebec'), (
        'Ungava Bay, Quebec, Canada',
    )),
    (('Americas', 'North America', 'Mexico'), (
        'Mexico City', 'Northwestern Mexico and Gulf of California, Mexico',
    )),
    (('Americas', 'North America', 'Caribbean'), ('Cuba', 'Puerto Rico')),
    (('Americas', 'South America'), (
        'Amazon Basin, South America', 'Andes, South America', 'Coastal Peru',
        'Orinoco and Casiquiare basin', 'Orinoco basin',
    )),
    (('Americas', 'South America', 'Ecuador'), ('Chimborazo', 'Galápagos Islands')),
    (('Americas', 'South America'), ('Ecuador', 'Peru')),
    (('Americas', 'South America', 'Venezuela'), ('Cumaná', 'Lake Valencia')),

    # Asia: historic names retained in leaf; modern states locate the place only.
    (('Asia', 'West Asia', 'Azerbaijan'), ('Baku',)),
    (('Asia', 'South Asia'), (
        'Bengal Delta, Bangladesh and India',
        'Ganges-Brahmaputra Delta, Bangladesh and India',
        'South Asia (India and Bay of Bengal)',
    )),
    (('Asia', 'South Asia', 'India'), (
        'Western Ghats, India', 'Madras (Chennai), India',
    )),
    (('Asia', 'South Asia', 'Pakistan'), ('Lahore',)),
    (('Asia', 'South Asia', 'Nepal'), ('Central Himalaya, Nepal',)),
    (('Asia', 'Himalaya'), ('Himalaya, Asia',)),
    (('Asia', 'Tibetan Plateau'), ('Tibetan Plateau, Asia',)),
    (('Asia', 'East Asia', 'China'), (
        'Beijing, China', 'Hainan, China', 'Hulu Cave, near Nanjing, Jiangsu, China',
        'Liuhe', 'Nanjing, China', 'Nanjing, Jiangsu',
        'Ningbo, China', 'Shanghai', 'Suzhou',
    )),
    (('Asia', 'East Asia', 'Japan'), (
        'Hiroshima, Japan', 'Nagasaki, Japan', 'Niigata, Japan',
        'Osaka', 'Tohoku, Japan',
    )),
    (('Asia', 'Southeast Asia', 'Vietnam'), ('Mekong Delta, Vietnam',)),
    (('Asia', 'Southeast Asia', 'Philippines'), ('Mount Pinatubo, Luzon, Philippines',)),

    # Africa and Oceania.
    (('Africa', 'North Africa', 'Egypt'), ('Giza, Egypt', 'Nile Delta, Egypt')),
    (('Africa', 'Northeast Africa', 'Sudan'), ('Khartoum, Sudan',)),
    (('Africa', 'West Africa', 'Nigeria'), ('Ibadan, Nigeria',)),
    (('Africa', 'Southeast Africa'), ('Mozambique',)),
    (('Africa', 'North Africa'), ('Sahara, North Africa',)),
    (('Africa', 'West Africa'), ('Sahel, West Africa',)),
    (('Oceania', 'Australia'), ('Darwin, Northern Territory, Australia',)),
    (('Oceania', 'Melanesia'), ('Papua New Guinea',)),
    (('Oceania', 'Polynesia', 'French Polynesia'), ('Tahiti, French Polynesia',)),

    # Land regions covering more than one country, water, ice and atmosphere.
    # 'Pacific' also names island cultures and coastal regions, not only the ocean.
    (('Cross-regional', 'Pacific region'), ('Pacific',)),
    (('Water bodies', 'Oceans', 'Atlantic Ocean'), (
        'Atlantic Ocean near 26.5°N', 'North Atlantic Ocean',
    )),
    (('Water bodies', 'Oceans', 'Pacific Ocean'), (
        'Eastern tropical Pacific Ocean', 'Equatorial Pacific Ocean',
        'North Pacific Ocean', 'Northeastern Pacific Ocean',
    )),
    (('Water bodies', 'Oceans', 'Indian Ocean'), ('Northern Indian Ocean',)),
    (('Water bodies', 'Oceans'), ('Arctic Ocean', 'Southern Ocean', 'Pacific Ocean')),
    (('Water bodies', 'Gulfs', 'Gulf of Mexico'), ('Northern Gulf of Mexico',)),
    (('Water bodies', 'Gulfs'), ('Gulf of Mexico',)),
    (('Water bodies', 'Bays'), (
        'Bay of Fundy, New Brunswick and Nova Scotia, Canada',
    )),
    (('Water bodies', 'Rivers', 'Mississippi River'), (
        'Mississippi River Basin, United States',
    )),
    (('Water bodies', 'Rivers'), ('Cumberland River', 'Tennessee River', 'Mississippi River')),
    (('Water bodies', 'Lakes', 'Lake Erie'), ('Lake Erie, North America',)),
    (('Water bodies', 'Bays'), ('Chesapeake Bay',)),
    (('Polar regions', 'Antarctica'), (
        'Antarctic coastal waters', 'Antarctic Peninsula, Antarctica',
        'Antarctic stratosphere', 'Dome C, Antarctica',
    )),
    (('Polar regions', 'Arctic'), ('Greenland',)),
]

PLACE_PATHS_EXTENSION = [
    [*parent, leaf]
    for parent, leaves in _GROUPS
    for leaf in leaves
]
