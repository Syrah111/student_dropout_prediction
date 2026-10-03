
MARITAL = dict(enumerate([
    "Single", "Married", "Widower", "Divorced", "Facto union", "Legally separated",
], start=1))

NATIONALITY = dict(enumerate([
    "Portuguese", "German", "Spanish", "Italian", "Dutch", "English", "Lithuanian",
    "Angolan", "Cape Verdean", "Guinean", "Mozambican", "Santomean", "Turkish",
    "Brazilian", "Romanian", "Moldovan", "Mexican", "Ukrainian", "Russian",
    "Cuban", "Colombian",
], start=1))

COURSE = dict(enumerate([
    "Biofuel Production Technologies", "Animation & Multimedia Design",
    "Social Service (evening)", "Agronomy", "Communication Design", "Veterinary Nursing",
    "Informatics Engineering", "Equinculture", "Management", "Social Service", "Tourism",
    "Nursing", "Oral Hygiene", "Advertising & Marketing Management",
    "Journalism & Communication", "Basic Education", "Management (evening)",
], start=1))

APP_MODE = dict(enumerate([
    "1st phase – general contingent", "Ordinance No. 612/93",
    "1st phase – special contingent (Azores)", "Holders of other higher courses",
    "Ordinance No. 854-B/99", "International student (bachelor)",
    "1st phase – special contingent (Madeira)", "2nd phase – general contingent",
    "3rd phase – general contingent", "Ordinance No. 533-A/99 b2 (different plan)",
    "Ordinance No. 533-A/99 b3 (other institution)", "Over 23 years old", "Transfer",
    "Change of course", "Technological specialization diploma holders",
    "Change of institution/course", "Short cycle diploma holders",
    "Change of institution/course (international)",
], start=1))

PREV_QUAL = dict(enumerate([
    "Secondary education", "Higher education – bachelor's degree", "Higher education – degree",
    "Higher education – master's degree", "Higher education – doctorate",
    "Frequency of higher education", "12th year – not completed", "11th year – not completed",
    "Other – 11th year of schooling", "10th year of schooling", "10th year – not completed",
    "Basic education 3rd cycle (9th–11th year)", "Basic education 2nd cycle (6th–8th year)",
    "Technological specialization course", "Higher education – degree (1st cycle)",
    "Professional higher technical course", "Higher education – master's degree (2nd cycle)",
], start=1))

QUALIFICATION = dict(enumerate([
    "Secondary education (12th year or equivalent)", "Higher education – bachelor's degree",
    "Higher education – degree", "Higher education – master's degree",
    "Higher education – doctorate", "Frequency of higher education",
    "12th year – not completed", "11th year – not completed", "7th year (old)",
    "Other – 11th year of schooling", "2nd year complementary high school course",
    "10th year of schooling", "General commerce course",
    "Basic education 3rd cycle (9th–11th year)", "Complementary high school course",
    "Technical-professional course", "Complementary high school course – not concluded",
    "7th year of schooling", "2nd cycle of the general high school course",
    "9th year – not completed", "8th year of schooling",
    "General course of administration and commerce", "Supplementary accounting and administration",
    "Unknown", "Cannot read or write", "Can read without a 4th year of schooling",
    "Basic education 1st cycle (4th/5th year)", "Basic education 2nd cycle (6th–8th year)",
    "Technological specialization course", "Higher education – degree (1st cycle)",
    "Specialized higher studies course", "Professional higher technical course",
    "Higher education – master's degree (2nd cycle)", "Higher education – doctorate (3rd cycle)",
], start=1))

OCCUPATION = dict(enumerate([
    "Student", "Legislative & executive bodies, directors and managers",
    "Specialists in intellectual & scientific activities", "Intermediate level technicians & professions",
    "Administrative staff", "Personal services, security & sales workers",
    "Farmers & skilled agriculture/fisheries/forestry workers",
    "Skilled industry, construction & craftsmen", "Machine operators & assembly workers",
    "Unskilled workers", "Armed forces professions", "Other situation", "Not specified",
    "Armed forces officers", "Armed forces sergeants", "Other armed forces personnel",
    "Directors of administrative & commercial services",
    "Hotel, catering, trade & other services directors",
    "Specialists in physical sciences, mathematics & engineering", "Health professionals",
    "Teachers", "Specialists in finance, accounting & administration",
    "Intermediate science & engineering technicians", "Intermediate health technicians",
    "Intermediate legal, social, sports & cultural technicians", "ICT technicians",
    "Office workers, secretaries & data processing operators",
    "Data, accounting, financial services & registry operators",
    "Other administrative support staff", "Personal service workers", "Sellers",
    "Personal care workers", "Protection & security personnel",
    "Market-oriented farmers & skilled agricultural workers",
    "Subsistence farmers, livestock keepers, fishermen & hunters",
    "Skilled construction workers (except electricians)",
    "Skilled metallurgy & metalworking workers", "Skilled electricity & electronics workers",
    "Food processing, woodworking & clothing workers", "Fixed plant & machine operators",
    "Assembly workers", "Vehicle drivers & mobile equipment operators",
    "Unskilled agriculture, animal production & forestry workers",
    "Unskilled extractive, construction, manufacturing & transport workers",
    "Meal preparation assistants", "Street vendors & street service providers",
], start=1))

assert (len(MARITAL), len(NATIONALITY), len(COURSE), len(APP_MODE),
        len(PREV_QUAL), len(QUALIFICATION), len(OCCUPATION)) == (6, 21, 17, 18, 17, 34, 46)
