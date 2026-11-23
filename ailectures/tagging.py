"""Explicit broader/narrower discovery paths; never infer from lecture prose.

The small compatibility vocabulary maps existing labels to subject/geographic
associations. Authors can supply additional tag_paths without a central registry.
Historical places stay historical; an unknown/ambiguous place remains flat.
"""
from .organization import topic_tags

# These are browsing associations, not borders, nationality, prerequisites, or
# a claim that a lecture covers every descendant of the broader label.
PLACE_PATHS = [
    ['Europe', 'France', 'Paris'], ['Europe', 'France', 'Lyon'], ['Europe', 'France', 'Auxerre'],
    ['Europe', 'Britain', 'England', 'London'], ['Europe', 'Britain', 'England', 'Oxford'],
    ['Europe', 'Britain', 'Scotland'], ['Europe', 'Britain', 'Wales'],
    ['Europe', 'Ireland', 'Dublin'], ['Europe', 'Italy', 'Florence'], ['Europe', 'Italy', 'Rome'],
    ['Europe', 'Italy', 'Venice'], ['Europe', 'Italy', 'Turin'],
    ['Europe', 'Germany', 'Berlin'], ['Europe', 'Germany', 'Göttingen'],
    ['Europe', 'Germany', 'Leipzig'], ['Europe', 'Germany', 'Hanover'],
    ['Europe', 'Switzerland', 'Basel'], ['Europe', 'Switzerland', 'Zürich'], ['Europe', 'Switzerland', 'Sion'],
    ['Europe', 'Austria', 'Vienna'], ['Europe', 'Hungary', 'Budapest'],
    ['Europe', 'Hungary', 'Szeged'], ['Europe', 'Hungary', 'Győr'],
    ['Europe', 'Czechia', 'Brno'], ['Europe', 'Czechia', 'Brünn'],
    ['Europe', 'Spain'], ['Europe', 'Portugal', 'Lisbon', 'Rua dos Douradores'], ['Europe', 'Denmark'], ['Europe', 'Finland'],
    ['Europe', 'Scandinavia', 'Denmark'], ['Europe', 'Scandinavia', 'Geatland'],
    ['Europe', 'Pyrenees'], ['Europe', 'Ancient Greece', 'Ithaca'],
    ['Eurasia', 'Aegean'], ['Asia', 'West Asia', 'Anatolia', 'Troy'],
    ['Asia', 'East Asia', 'Japan', 'Kyoto'], ['North America', 'United States', 'Alabama'],
    ['Europe', 'Iceland'], ['Europe', 'Ukraine'], ['Europe', 'Eastern Europe'],
    ['Eurasia', 'Russia'], ['Eurasia', 'Russia', 'Moscow'], ['Eurasia', 'Russia', 'Saint Petersburg'],
    ['Asia', 'East Asia', 'China', 'Dunhuang'], ['Asia', 'East Asia', 'Japan', 'Tokyo'],
    ['Asia', 'East Asia', 'Korea'], ['Asia', 'East Asia', 'Goryeo'],
    ['Asia', 'South Asia', 'India'], ['Asia', 'South Asia', 'Pakistan'],
    ['Asia', 'South Asia', 'Tamil regions'], ['Asia', 'South Asia', 'Bay of Bengal'],
    ['Asia', 'Southeast Asia', 'Vietnam'], ['Asia', 'Southeast Asia', 'Cambodia'],
    ['Asia', 'Southeast Asia', 'Laos'], ['Asia', 'Southeast Asia', 'Indonesia', 'Java'],
    ['Asia', 'Southeast Asia', 'Indonesia', 'Bali'], ['Asia', 'Southeast Asia', 'Indonesia', 'Sulawesi'],
    ['Asia', 'Southeast Asia', 'Indonesia', 'Bandung'], ['Asia', 'Southeast Asia', 'Philippines', 'Manila'],
    ['Asia', 'West Asia', 'Iraq', 'Baghdad'], ['Asia', 'West Asia', 'Mesopotamia', 'Sumer', 'Uruk'],
    ['Asia', 'West Asia', 'Mesopotamia', 'Babylonia'], ['Asia', 'Afghanistan'],
    ['Africa', 'North Africa', 'Egypt', 'Alexandria'], ['Africa', 'North Africa', 'Ancient Egypt'],
    ['Africa', 'North Africa', 'Algeria'], ['Africa', 'West Africa', 'Mali', 'Timbuktu'],
    ['Africa', 'East Africa', 'Ethiopia'], ['Africa', 'East Africa', 'Kilwa'],
    ['Africa', 'East Africa', 'Madagascar'], ['Africa', 'East Africa', 'Rwanda'], ['Africa', 'South Africa'],
    ['North America', 'United States', 'New York'], ['North America', 'United States', 'New York City'],
    ['North America', 'United States', 'Massachusetts', 'Boston'],
    ['North America', 'United States', 'Massachusetts', 'Concord'],
    ['North America', 'United States', 'Kentucky'], ['North America', 'United States', 'Ohio'],
    ['North America', 'United States', 'Louisiana'], ['North America', 'United States', 'Pennsylvania'],
    ['North America', 'United States', 'New England'],
    ['North America', 'United States', 'Alaska'],
    ['North America', 'United States', 'California', 'Mojave Desert'],
    ['North America', 'United States', 'California', 'Santa Monica, California'],
    ['North America', 'United States', 'California', 'Berkeley, California'],
    ['North America', 'United States', 'Illinois', 'Chicago'],
    ['North America', 'United States', 'Illinois', 'Centralia, Illinois'],
    ['North America', 'United States', 'Illinois', 'Urbana, Illinois'],
    ['North America', 'United States', 'New Jersey', 'Princeton, New Jersey'],
    ['North America', 'United States', 'Louisiana', 'Baton Rouge, Louisiana'],
    ['North America', 'United States', 'Georgia', 'Atlanta, Georgia'],
    ['North America', 'United States', 'Washington, D.C.'],
    ['North America', 'United States', 'Massachusetts', 'Cambridge (Massachusetts)'],
    ['Europe', 'Britain', 'England', 'Cambridge (England)'],
    ['Europe', 'Britain', 'England', 'Terling'], ['Europe', 'Britain', 'England', 'Woolsthorpe'],
    ['Europe', 'Netherlands', 'The Hague'], ['Europe', 'Netherlands', 'Leiden'], ['Europe', 'Netherlands', 'Breda'],
    ['Europe', 'Italy', 'Messina, Italy'],
    ['Europe', 'Italy', 'Trieste'], ['Europe', 'Switzerland', 'Zug'],
    ['Asia', 'East Asia', 'Japan', 'Iga Province'], ['Asia', 'East Asia', 'Japan', 'Kōka'],
    ['Asia', 'East Asia', 'Japan', 'Edo'], ['Asia', 'East Asia', 'Japan', 'Edo (Tokyo)'],
    ['Asia', 'South Asia', 'India', 'Madras'],

    ['Europe', 'France', 'Digne'], ['Europe', 'France', 'Montreuil-sur-Mer'], ['Europe', 'France', 'Montfermeil'], ['North America', 'United States', 'Princeton'],
    ['North America', 'United States', 'Chapel Hill'], ['North America', 'United States', 'Baltimore'],
    ['North America', 'United States', 'Berkeley'], ['North America', 'Canada', 'Toronto'],
    ['North America', 'Mexico'], ['Americas', 'Caribbean', 'Haiti'], ['Americas', 'Latin America'],
    ['Americas', 'Mesoamerica'], ['Americas', 'Andes'], ['Oceania', 'Australia'], ['Pacific', 'Hawaii'],
    ['Europe', 'Ancient Greece'], ['Europe', 'Ancient Rome'],
]


# Regional associations do not imply modern nationality or historical borders.
# Historic-place checks: UNESCO Soltaniyeh (whc.unesco.org/en/list/1188),
# Samarkand (whc.unesco.org/en/list/603), Ugarit (tentativelists/1292),
# and Brubaker et al., Nationalist Politics and Everyday Ethnicity, chapter 3
# (doi:10.1515/9780691187792-010), on Kolozsvár/Transylvania.
# Context-dependent names (Cambridge, Great Lakes, Plains) belong in authored
# pack-local paths rather than this global vocabulary.
PLACE_PATHS += [
    ['Asia', 'West Asia', 'Levant', 'Ugarit'],
    ['Asia', 'South Asia', 'Indus'],
    ['Asia', 'West Asia', 'Iran', 'Soltaniyeh'],
    ['Asia', 'Central Asia', 'Samarqand'],
    ['Asia', 'Southeast Asia', 'East Timor'],
    ['Africa', 'Northeast Africa', 'Sudan'], ['Africa', 'Nile'],
    ['Africa', 'Central Africa', 'Congo'],
    ['Africa', 'Northeast Africa', 'Kush'], ['Africa', 'Northeast Africa', 'Aksum', 'Adulis'],
    ['Africa', 'East Africa', 'Swahili Coast'], ['Africa', 'East Africa', 'Kenya'],
    ['Africa', 'East Africa', 'Tanzania'], ['Africa', 'East Africa', 'Uganda'],
    ['Africa', 'East Africa', 'Malawi'], ['Africa', 'South-central Africa', 'Zambia'],
    ['Africa', 'Southern Africa', 'Zimbabwe', 'Great Zimbabwe'],
    ['Africa', 'Southern Africa', 'Rhodesia'], ['Africa', 'Southern Africa', 'South Africa', 'Mapungubwe'],
    ['Africa', 'Central Africa', 'Congo Basin'], ['Africa', 'Central Africa', 'Kingdom of Kongo'],
    ['Africa', 'Sahel'], ['Africa', 'West Africa', 'Ghana Empire'],
    ['Africa', 'West Africa', 'Ghana'], ['Africa', 'West Africa', 'Mauritania'],
    ['Africa', 'West Africa', 'Nigeria', 'Zaria'],
    ['Africa', 'West Africa', 'Nigeria', 'Onitsha'],
    ['Africa', 'West Africa', 'Nigeria', 'Lagos'],
    ['Africa', 'West Africa', 'Nigeria', 'Ibadan'],
    ['Europe', 'Northern Europe', 'Karelia'],
    ['Europe', 'Transylvania', 'Kolozsvár'],
    ['Europe', 'Balkans', 'Yugoslavia'], ['Europe', 'Balkans', 'Kosovo'],
    ['Americas', 'South America', 'Argentina', 'Mendoza'],
    ['Americas', 'South America', 'Argentina', 'Buenos Aires'],
    ['Americas', 'South America', 'Andes', 'Potosí'],
    ['Americas', 'North America', 'Central America', 'Panama'],
    ['Cross-regional', 'Middle East'], ['Cross-regional', 'Arab World'],
    ['Cross-regional', 'Mediterranean', 'Hellenistic Mediterranean'],
    ['Cross-regional', 'Mediterranean', 'Eastern Mediterranean', 'Cyprus'],
    ['Water bodies', 'Oceans', 'Atlantic'],
    ['Water bodies', 'Oceans', 'Indian Ocean'],
    ['Water bodies', 'Seas', 'Red Sea'],
    ['Polar regions', 'Arctic'], ['Antarctica'],
]

# Use complete paths consistently, including existing city and regional paths.
# Matching adds ancestors only; a broad Americas tag cannot acquire countries.
def _geographic_branch(path):
    if path[0] == 'North America':
        return ['Americas', *path]
    if path[:2] == ['Americas', 'Caribbean']:
        return ['Americas', 'North America', *path[1:]]
    if path[:2] == ['Americas', 'Andes']:
        return ['Americas', 'South America', *path[1:]]
    if path == ['Pacific', 'Hawaii']:
        return ['Oceania', 'Polynesia', 'Hawaii']
    if path[0] == 'Pacific':
        return ['Water bodies', 'Oceans', *path]
    return path

PLACE_PATHS = [_geographic_branch(path) for path in PLACE_PATHS]

# Exact authored place labels with vetted broader paths.
from .place_hierarchy_extended import PLACE_PATHS_EXTENSION
PLACE_PATHS.extend(PLACE_PATHS_EXTENSION)

TOPIC_PATHS = [
    ['Science', 'Biology', 'Cell biology', 'Cell structure'],
    ['Science', 'Biology', 'Cell biology', 'Cell membranes'],
    ['Science', 'Biology', 'Genetics', 'Inheritance'], ['Science', 'Biology', 'Genetics', 'Meiosis'],
    ['Science', 'Biology', 'Molecular biology', 'DNA'],
    ['Science', 'Biology', 'Molecular biology', 'Gene expression'],
    ['Science', 'Biology', 'Biochemistry', 'Metabolism'],
    ['Science', 'Physics', 'Classical mechanics', 'Conservation laws'],
    ['Science', 'Physics', 'Thermodynamics'], ['Science', 'Physics', 'Electromagnetism'],
    ['Science', 'Physics', 'Quantum mechanics'], ['Science', 'Physics', 'Relativity'],
    ['Science', 'Physics', 'Waves'], ['Science', 'Astronomy'], ['Science', 'Geology'],
    ['Mathematics', 'Analysis', 'Calculus', 'Multivariable calculus'],
    ['Mathematics', 'Analysis', 'Functional analysis', 'Operator theory'],
    ['Mathematics', 'Analysis', 'Harmonic analysis', 'Fourier analysis', 'Fourier transform'],
    ['Mathematics', 'Analysis', 'Harmonic analysis', 'Fourier analysis', 'Fourier series'],
    ['Mathematics', 'Differential equations', 'Ordinary differential equations'],
    ['Mathematics', 'Differential equations', 'Partial differential equations'],
    ['Mathematics', 'Numerical analysis', 'Numerical differential equations'],
    ['Mathematics', 'Analysis', 'Functional analysis', 'Operator theory', 'Spectral theory'],
    ['Mathematics', 'Linear algebra', 'Eigenvalues'],
    ['Mathematics', 'Geometry'], ['Mathematics', 'Topology'],
    ['Mathematics', 'Probability', 'Measure theory'], ['Mathematics', 'Statistics', 'Causal inference'],
    ['Mathematics', 'Discrete mathematics', 'Graph theory'], ['Mathematics', 'Logic', 'Type theory'],
    ['Mathematics', 'Category theory'], ['Mathematics', 'Optimization', 'Convex optimization'],
    ['Computing', 'Signal processing', 'Sampling', 'Aliasing'],
    ['Computing', 'Signal processing', 'Discrete Fourier transform', 'Fast Fourier transform'],
    ['Arts', 'Literature', 'Fiction', 'Novels'], ['Arts', 'Literature', 'Fiction', 'Short stories'],
    ['Arts', 'Literature', 'Poetry', 'Epic'], ['Arts', 'Literature', 'Drama'],
    ['Arts', 'Literature', 'Fiction', 'Fables'], ['Arts', 'Literature', 'Saga'],
    ['Arts', 'Literature', 'Oral traditions'], ['Arts', 'Literature', 'Literary analysis'], ['Arts', 'Literature', 'Prose fragments'],
    ['Arts', 'Literature', 'Creative writing', 'Fiction writing'],
    ['Arts', 'Music', 'Music theory'], ['Arts', 'Music', 'Audio production'],
    ['History', 'History of science and mathematics', 'History of mathematics'],
    ['Science', 'Biology', 'Cell biology', 'Microscopy'],
    ['Science', 'Biology', 'Cell biology', 'Organelles'],
    ['Science', 'Biology', 'Cell biology', 'Endosymbiosis'],
    ['Science', 'Biology', 'Cell biology', 'Membrane biology', 'Osmosis'],
    ['Science', 'Biology', 'Cell biology', 'Membrane biology', 'Active transport'],
    ['Science', 'Biology', 'Biochemistry', 'Chemiosmosis'],
    ['Science', 'Biology', 'Molecular biology', 'RNA', 'RNA splicing'],
    ['Science', 'Biology', 'Molecular biology', 'Protein synthesis'],
    ['Science', 'Biology', 'Molecular biology', 'Gene regulation', 'Epigenetics'],
    ['Science', 'Biology', 'Genetics', 'DNA replication'],
    ['Science', 'Biology', 'Genetics', 'DNA repair'],
    ['Science', 'Biology', 'Genetics', 'Chromosomes', 'Recombination'],
    ['Science', 'Biology', 'Genetics', 'Mitosis'],
    ['Science', 'Physics', 'Optics', 'Interference'],
    ['Science', 'Physics', 'Optics', 'Diffraction'],
    ['Science', 'Physics', 'Thermal physics', 'Statistical mechanics', 'Entropy'],
    ['Science', 'Physics', 'Thermal physics', 'Phase transitions', 'Critical phenomena'],
    ['Science', 'Physics', 'Oscillators', 'Resonance'],
    ['Computing', 'Signal processing', 'Sampling', 'Nyquist frequency'],
    ['Computing', 'Signal processing', 'Spectral analysis', 'Spectral leakage'],
    ['Computing', 'Signal processing', 'Spectral analysis', 'Window functions'],
    ['Computing', 'Signal processing', 'Spectral analysis', 'Frequency resolution'],
    ['Mathematics', 'Numerical analysis', 'Finite differences', 'Upwind scheme'],
    ['Mathematics', 'Numerical analysis', 'Finite-volume methods'],
    ['Mathematics', 'Numerical analysis', 'Numerical stability', 'CFL condition'],
    ['Mathematics', 'Numerical analysis', 'Spectral methods'],
    ['Mathematics', 'Differential equations', 'Partial differential equations', 'Transport equation'],
    ['History', 'Archaeology'], ['History', 'World history'],
    ['Practical skills', 'Trades', 'Electrical work'], ['Practical skills', 'Trades', 'Masonry'],
]


def normalize_paths(value):
    """Malformed optional paths are ignored rather than hiding usable content."""
    if not isinstance(value, list):
        return []
    result = []
    for path in value[:64]:
        if not isinstance(path, list) or not 1 <= len(path) <= 8:
            continue
        labels = topic_tags(path)
        if len(labels) != len(path):
            continue  # Includes duplicate/cyclic labels and invalid labels.
        if labels not in result:
            result.append(labels)
    return result


def tag_key(label):
    aliases = {'dft': 'discrete fourier transform', 'fft': 'fast fourier transform',
               'pde': 'partial differential equations', 'ode': 'ordinary differential equations'}
    value = label.casefold().replace('-', ' ').replace('_', ' ')
    return aliases.get(value, value)


def vocabulary_index(vocabulary, prefix=''):
    indexed = {}
    for path in vocabulary:
        for index, label in enumerate(path):
            branch = tuple(prefix + part for part in path[:index+1])
            branches = indexed.setdefault(tag_key(label), [])
            if branch not in branches:
                branches.append(branch)
    return indexed


_TOPIC_INDEX = vocabulary_index(TOPIC_PATHS)
_PLACE_INDEX = vocabulary_index(PLACE_PATHS, 'Place: ')


def matching_paths(labels, vocabulary, prefix=''):
    """A broad authored label never acquires narrower, unrecorded coverage."""
    if vocabulary is TOPIC_PATHS and not prefix:
        indexed = _TOPIC_INDEX
    elif vocabulary is PLACE_PATHS and prefix == 'Place: ':
        indexed = _PLACE_INDEX
    else:
        indexed = vocabulary_index(vocabulary, prefix)
    result = []
    for label in labels:
        result.extend(list(path) for path in indexed.get(tag_key(label), [(prefix + label,)]))
    return result


def tag_paths(tags, places, authored=()):
    facets = ('Place: ', 'Period: ', 'Author: ', 'Work date: ', 'Historical period: ',
              'Story setting: ', 'Lifetime: ', 'Surviving witness: ', 'Composition date: ', 'Historical setting: ')
    topics = [tag for tag in tags if not tag.startswith(facets)]
    geography = list(dict.fromkeys([*places, *(tag[7:] for tag in tags if tag.startswith('Place: '))]))
    paths = matching_paths(topics, TOPIC_PATHS) + matching_paths(geography, PLACE_PATHS, 'Place: ')
    for path in normalize_paths(authored):
        if path[0].startswith('Place: '):
            # Older packs may start at North America or another known region.
            # Complete the head's ancestors without changing authored children.
            parents = matching_paths([path[0][7:]], PLACE_PATHS, 'Place: ')
            for parent in parents:
                complete = parent + path[1:]
                if len(complete) <= 8 and len(set(complete)) == len(complete):
                    paths.append(complete)
                else:
                    paths.append(path)
        else:
            paths.append(path)
    # Suppress prefixes that are already represented by a more specific path.
    unique = list(dict.fromkeys(tuple(path) for path in paths))
    return [list(path) for path in unique if not any(
        len(other) > len(path) and (other[:len(path)] == path or (len(path) == 1 and path[0] in other))
        for other in unique)]
