# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import scrapy
import re

class NewsbotSpider(scrapy.Spider):
    name = 'newsbot'
    allowed_domains = ['https://www.express.co.uk']
    start_urls = ['https://www.express.co.uk']

    start_urls = ["https://www.express.co.uk",
	"https://www.express.co.uk/feeds",
	"https://www.express.co.uk/users/login",
	"https://www.express.co.uk/users/register",
	"https://www.express.co.uk/horoscope",
	"https://www.express.co.uk/our-apps",
	"https://www.express.co.uk/life-style/top10facts",
	"https://www.express.co.uk/ourpaper",
	"https://www.express.co.uk/paper-archive",
	"https://www.express.co.uk/news/weather",
	"https://www.express.co.uk/news",
	"https://www.express.co.uk/showbiz",
	"https://www.express.co.uk/sport",
	"https://www.express.co.uk/comment",
	"https://www.express.co.uk/finance",
	"https://www.express.co.uk/travel",
	"https://www.express.co.uk/entertainment",
	"https://www.express.co.uk/life-style",
	"https://www.express.co.uk/life-style/life",
	"https://www.express.co.uk/life-style/style",
	"https://www.express.co.uk/life-style/health",
	"https://www.express.co.uk/life-style/cars",
	"https://www.express.co.uk/life-style/garden",
	"https://www.express.co.uk/life-style/food",
	"https://www.express.co.uk/life-style/property",
	"https://www.express.co.uk/life-style/diets",
	"https://www.express.co.uk/life-style/science-technology",
	"https://www.express.co.uk/life-style/saturday",
	"https://www.express.co.uk/life-style/competitions",
	"https://www.express.co.uk/life-style/s-mag",
	"https://www.express.co.uk/news/uk",
	"https://www.express.co.uk/news/world",
	"https://www.express.co.uk/news/politics",
	"https://www.express.co.uk/news/nature",
	"https://www.express.co.uk/news/royal",
	"https://www.express.co.uk/news/history",
	"https://www.express.co.uk/news/obituaries",
	"https://www.express.co.uk/news/sunday",
	"https://www.express.co.uk/news/weird",
	"https://www.express.co.uk/news/science",
	"https://www.express.co.uk/scotland",
	"https://www.express.co.uk/sport/football",
	"https://www.express.co.uk/sport/football/stats",
	"https://www.express.co.uk/transfernews",
	"https://www.express.co.uk/sport/tennis",
	"https://www.express.co.uk/sport/boxing",
	"https://www.express.co.uk/sport/ufc",
	"https://www.express.co.uk/sport/f1-autosport",
	"https://www.express.co.uk/sport/cricket",
	"https://www.express.co.uk/sport/golf",
	"https://www.express.co.uk/sport/rugbyunion",
	"https://www.express.co.uk/sport/horseracing",
	"https://www.express.co.uk/sport/othersport",
	"https://www.express.co.uk/latest",
	"https://www.express.co.uk/entities",
	"https://www.express.co.uk/latest/asda",
	"https://www.express.co.uk/latest/tesco",
	"https://www.express.co.uk/finance/city",
	"https://www.express.co.uk/finance/personalfinance",
	"https://www.express.co.uk/finance/retirement",
	"https://www.express.co.uk/finance/crusader",
	"https://www.express.co.uk/latest/brexit",
	"https://www.express.co.uk/latest/eu-referendum",
	"https://www.express.co.uk/latest/European-Union",
	"https://www.express.co.uk/latest/european-union",
	"https://www.express.co.uk/latest/theresa-may",
	"https://www.express.co.uk/latest/david-cameron",
	"https://www.express.co.uk/latest/barack-obama",
	"https://www.express.co.uk/latest/donald-trump",
	"https://www.express.co.uk/latest/united-states",
	"https://www.express.co.uk/latest/us-election-2016",
	"https://www.express.co.uk/latest/hillary-clinton",
	"https://www.express.co.uk/latest/angela-merkel",
	"https://www.express.co.uk/latest/germany",
	"https://www.express.co.uk/latest/queen",
	"https://www.express.co.uk/latest/kate-middleton",
	"https://www.express.co.uk/latest/prince-william",
	"https://www.express.co.uk/latest/prince-charles",
	"https://www.express.co.uk/latest/royal-family",
	"https://www.express.co.uk/latest/prince-george",
	"https://www.express.co.uk/latest/meghan-markle",
	"https://www.express.co.uk/latest/prince-harry",
	"https://www.express.co.uk/latest/princess-diana",
	"https://www.express.co.uk/latest/diesel",
	"https://www.express.co.uk/latest/cancer",
	"https://www.express.co.uk/latest/prostate-cancer",
	"https://www.express.co.uk/latest/dementia",
	"https://www.express.co.uk/latest/diabetes",
	"https://www.express.co.uk/latest/youtube",
	"https://www.express.co.uk/celebrity-news",
	"https://www.express.co.uk/showbiz/tv-radio",
	"https://www.express.co.uk/latest/premier-league",
	"https://www.express.co.uk/pictures",
	"https://www.express.co.uk/pictures/pics",
	"https://www.express.co.uk/pictures/celebrity",
	"https://www.express.co.uk/pictures/sport",
	"https://www.express.co.uk/pictures/royal",
	"https://www.express.co.uk/pictures/royal?o=3",
	"https://www.express.co.uk/pictures/pics?o=3",
	"https://www.express.co.uk/comment/expresscomment",
	"https://www.express.co.uk/comment/columnists",
	"https://www.express.co.uk/comment/beachcomber",
	"https://www.express.co.uk/search?s=&section=107",
	"https://www.express.co.uk/latest/star-wars",
	"https://www.express.co.uk/entertainment/films",
	"https://www.express.co.uk/entertainment/gaming",
	"https://www.express.co.uk/entertainment/theatre",
	"https://www.express.co.uk/entertainment/books",
	"https://www.express.co.uk/entertainment/music",
	"https://www.express.co.uk/puzzles",
	"https://www.express.co.uk/travel/cruise",
	"https://www.express.co.uk/travel/activity",
	"https://www.express.co.uk/travel/beach",
	"https://www.express.co.uk/travel/shortbreaks",
	"https://www.express.co.uk/travel/articles",
	"https://www.express.co.uk/sitemap",
	"https://www.express.co.uk/latest/north-korea",
	"https://www.express.co.uk/sitearchive",
	"https://www.express.co.uk/contact",
	"http://www.express.co.uk/advertise",
	"http://www.express.co.uk/supportticket",
	"http://www.express.co.uk/privacy",
	"http://www.express.co.uk/cookie-policy",
	"http://www.express.co.uk/terms-and-conditions",
	"http://www.express.co.uk/news/clarifications-corrections",
	"http://www.express.co.uk/contactus",
	"http://www.express.co.uk/contactform/corrections",
	"https://www.express.co.uk/preferences",
	"http://www.express.co.uk/contactform/comment/daily-star",
	"http://www.express.co.uk/contactform/comment/daily-star-sunday",
	"http://www.express.co.uk/contactform/comment/daily-express",
	"http://www.express.co.uk/contactform/comment/sunday-express",
	"http://www.express.co.uk/complaints-policy",
	"http://www.express.co.uk/contactform/complaints",
	"https://www.express.co.uk/latest/iran",
	"https://www.express.co.uk/latest/india",
	"https://www.express.co.uk/latest/china",
	"http://www.express.co.uk/latest/world-war-3",
	"http://www.express.co.uk/latest/russia",
	"http://www.express.co.uk/latest/vladimir-putin",
	"http://www.express.co.uk/life-style/competitions?utm_source=trending&utm_campaign=comps&utm_medium=link",
	"https://www.express.co.uk/weather"]
	
	
	
    start_urls =["http://www.independent.co.uk",
"http://www.independent.co.uk/news",
"http://www.independent.co.uk/news/uk/politics",
"http://www.independent.co.uk/topic/brexit",
"http://www.independent.co.uk/news/uk",
"http://www.independent.co.uk/news/world/americas",
"http://www.independent.co.uk/news/world",
"http://www.independent.co.uk/news/science",
"http://www.independent.co.uk/news/health",
"http://www.independent.co.uk/news/media",
"http://www.independent.co.uk/news/obituaries",
"http://www.independent.co.uk/news/long_reads",
"http://www.independent.co.uk/infact",
"http://www.independent.co.uk/voices",
"http://www.independent.co.uk/author/shappi-khorsandi",
"http://www.independent.co.uk/author/mary-dejevsky",
"http://www.independent.co.uk/author/andrew-grice",
"http://www.independent.co.uk/author/robert-fisk",
"http://www.independent.co.uk/author/john-rentoul",
"http://www.independent.co.uk/author/mark-steel",
"http://www.independent.co.uk/life-style",
"http://www.independent.co.uk/life-style/gadgets-and-tech",
"http://www.independent.co.uk/travel",
"http://www.independent.co.uk/life-style/fashion",
"http://www.independent.co.uk/life-style/food-and-drink",
"http://www.independent.co.uk/life-style/food-and-drink/recipes",
"http://www.independent.co.uk/money",
"http://www.independent.co.uk/life-style/health-and-families",
"http://www.independent.co.uk/extras/indybest",
"http://www.independent.co.uk/life-style/love-sex",
"http://www.independent.co.uk/sport",
"http://www.independent.co.uk/sport/cricket/ashes",
"http://www.independent.co.uk/topic/football-transfers",
"http://www.independent.co.uk/sport/football",
"http://www.independent.co.uk/sport/rugby/rugby-union",
"http://www.independent.co.uk/sport/cricket",
"http://www.independent.co.uk/sport/tennis",
"http://www.independent.co.uk/sport/golf",
"http://www.independent.co.uk/sport/motor-racing/formula1",
"http://www.independent.co.uk/sport/general/boxing",
"http://www.independent.co.uk/sport/us-sport",
"http://www.independent.co.uk/news/business",
"http://www.independent.co.uk/news/business/indyventure",
"http://www.independent.co.uk/video",
"http://www.independent.co.uk/arts-entertainment",
"http://www.independent.co.uk/arts-entertainment/tv",
"http://www.independent.co.uk/arts-entertainment/films",
"http://www.independent.co.uk/arts-entertainment/music",
"http://www.independent.co.uk/arts-entertainment/books",
"http://www.independent.co.uk/arts-entertainment/art",
"http://www.independent.co.uk/arts-entertainment/theatre-dance",
"http://www.independent.co.uk/login",
"http://www.independent.co.uk/register",
"http://www.independent.co.uk/news/people",
"http://www.independent.co.uk/news/homelesshelpline",
"http://www.independent.co.uk/author/janet-street-porter",
"http://www.independent.co.uk/author/holly-baxter",
"http://www.independent.co.uk/voices/campaigns",
"http://www.independent.co.uk/voices/comment",
"http://www.independent.co.uk/voices/editorials",
"http://www.independent.co.uk/voices/letters",
"http://www.independent.co.uk/sport/motor-racing",
"http://www.independent.co.uk/sport/general/rugby-league",
"http://www.independent.co.uk/arts-entertainment/comedy",
"http://www.independent.co.uk/life-style/motoring",
"http://www.independent.co.uk/student",
"http://www.independent.co.uk/topic/iphone",
"http://www.independent.co.uk/life-style/gadgets-and-tech/news",
"http://www.independent.co.uk/life-style/gadgets-and-tech/features",
"http://www.independent.co.uk/life-style/gadgets-and-tech/gaming",
"http://www.independent.co.uk/video/News",
"http://www.independent.co.uk/video/Explainers",
"http://www.independent.co.uk/video/Sport",
"http://www.independent.co.uk/video/People-and-culture",
"http://www.independent.co.uk/extras/indybest/outdoor-activity",
"http://www.independent.co.uk/extras/indybest/house-garden",
"http://www.independent.co.uk/extras/indybest/kids",
"http://www.independent.co.uk/extras/indybest/books",
"http://www.independent.co.uk/extras/indybest/travel",
"http://www.independent.co.uk/extras/indybest/fashion-beauty",
"http://www.independent.co.uk/extras/indybest/food-drink",
"http://www.independent.co.uk/extras/indybest/gadgets-tech",
"http://www.independent.co.uk/money/mortgages",
"http://www.independent.co.uk/money/loans-credit",
"http://www.independent.co.uk/money/spend-save",
"http://www.independent.co.uk/money/pensions",
"http://www.independent.co.uk/money/hifx-international-money-transfers?icn=hifx_nav",
"http://www.independent.co.uk/money/health-insurance?icn=axa_nav",
"http://www.independent.co.uk/money/moneydeals",
"http://www.independent.co.uk/extras",
"http://www.independent.co.uk/news/corrections",
"http://www.independent.co.uk/marketing/apps",
"http://www.independent.co.uk/independentbooks",
"http://www.independent.co.uk/competitions?icn=offfers_nav",
"http://www.independent.co.uk/competitions",
"http://www.independent.co.uk/topic/christmas-shopping",
"http://www.independent.co.uk/author/kate-hughes",
"http://www.independent.co.uk/author-list",
"http://www.independent.co.uk/topic/slaves-on-our-streets",
"http://www.independent.co.uk/news/uk/crime",
"http://www.independent.co.uk/author/lizzie-dearden",
"http://www.independent.co.uk/topic/acid-attacks",
"http://www.independent.co.uk/news/uk/home-news",
"http://www.independent.co.uk/author/caroline-mortimer",
"http://www.independent.co.uk/news/world/asia",
"http://www.independent.co.uk/author/staff-and-agenices",
"http://www.independent.co.uk/news/world/europe",
"http://www.independent.co.uk/author/jon-stone",
"http://www.independent.co.uk/topic/daviddavis",
"http://www.independent.co.uk/author/shehab-khan",
"http://www.independent.co.uk/topic/jeremy-hunt",
"http://www.independent.co.uk/author/alex-matthews-king",
"http://www.independent.co.uk/topic/China",
"http://www.independent.co.uk/author/andrew-griffin",
"http://www.independent.co.uk/extras/indybest/house-garden/kitchen-appliances",
"http://www.independent.co.uk/extras/indybest/house-garden/toasters",
"http://www.independent.co.uk/extras/indybest/house-garden/coffee",
"http://www.independent.co.uk/extras/indybest/house-garden/household-appliances",
"http://www.independent.co.uk/extras/indybest/house-garden/vacuum-cleaners",
"http://www.independent.co.uk/extras/indybest/house-garden/lighting",
"http://www.independent.co.uk/extras/indybest/house-garden/powertools",
"http://www.independent.co.uk/extras/indybest/house-garden/furniture",
"http://www.independent.co.uk/extras/indybest/house-garden/bedroom",
"http://www.independent.co.uk/extras/indybest/house-garden/mattresses",
"http://www.independent.co.uk/extras/indybest/house-garden/bathroom",
"http://www.independent.co.uk/extras/indybest/house-garden/kitchen-accessories",
"http://www.independent.co.uk/extras/indybest/house-garden/dining",
"http://www.independent.co.uk/extras/indybest/house-garden/home-fragrances",
"http://www.independent.co.uk/extras/indybest/house-garden/garden-furniture",
"http://www.independent.co.uk/extras/indybest/house-garden/gardening",
"http://www.independent.co.uk/author/grace-dent",
"http://www.independent.co.uk/topic/Alcohol",
"http://www.independent.co.uk/author/ketan-patel",
"http://www.independent.co.uk/service",
"http://www.independent.co.uk/user-profile",
"http://www.independent.co.uk/search/site",
"http://www.independent.co.uk/hc/en-us",
"http://www.independent.co.uk/hc/en-us/requests/new",
"http://www.independent.co.uk/hc/en-us/signin?re",
"http://www.independent.co.uk/news/business/news",
"http://www.independent.co.uk/author/stephen-little",
"http://www.independent.co.uk/topic/Inflation",
"http://www.independent.co.uk/author/alan-jones-2",
"http://www.independent.co.uk/topic/cbi",
"http://www.independent.co.uk/author/joe-watts",
"http://www.independent.co.uk/videos",
"http://www.independent.co.uk/author/matt-murphy",
"http://www.independent.co.uk/sport/football/premier-league",
"http://www.independent.co.uk/author/jack-de-menezes",
"http://www.independent.co.uk/topic/bo-scarbrough",
"http://www.independent.co.uk/topics-list",
"http://www.independent.co.uk/topics-list/a",
"http://www.independent.co.uk/topics-list/b",
"http://www.independent.co.uk/topics-list/c",
"http://www.independent.co.uk/topics-list/d",
"http://www.independent.co.uk/topics-list/e",
"http://www.independent.co.uk/topics-list/f",
"http://www.independent.co.uk/topics-list/g",
"http://www.independent.co.uk/topics-list/h",
"http://www.independent.co.uk/topics-list/i",
"http://www.independent.co.uk/topics-list/j",
"http://www.independent.co.uk/topics-list/k",
"http://www.independent.co.uk/topics-list/l",
"http://www.independent.co.uk/topics-list/m",
"http://www.independent.co.uk/topics-list/n",
"http://www.independent.co.uk/topics-list/o",
"http://www.independent.co.uk/topics-list/p",
"http://www.independent.co.uk/topics-list/q",
"http://www.independent.co.uk/topics-list/r",
"http://www.independent.co.uk/topics-list/s",
"http://www.independent.co.uk/topics-list/t",
"http://www.independent.co.uk/topics-list/u",
"http://www.independent.co.uk/topics-list/v",
"http://www.independent.co.uk/topics-list/w",
"http://www.independent.co.uk/topics-list/x",
"http://www.independent.co.uk/topics-list/y",
"http://www.independent.co.uk/topics-list/z",
"http://www.independent.co.uk/topics-list/%5C",
"http://www.independent.co.uk/topics-list/%5D",
"http://www.independent.co.uk/archive",
"http://www.independent.co.uk/archive/2018-01-01",
"http://www.independent.co.uk/author/lizzy-buchan",
"http://www.independent.co.uk/topic/justine-greening",
"http://www.independent.co.uk/author/jane-merrick",
"http://www.independent.co.uk/topic/DavidDavis",
"http://www.independent.co.uk/author/ashley-cowburn",
"http://www.independent.co.uk/voices/campaigns/voicesindanger",
"http://www.independent.co.uk/author/phoebe-braithwaite",
"http://www.independent.co.uk/topic/TheresaMay",
"http://www.independent.co.uk/author/rob-merrick",
"http://www.independent.co.uk/author/jacob-stolworthy",
"http://www.independent.co.uk/arts-entertainment/films/features",
"http://www.independent.co.uk/author/kaleem-aftab-0",
"http://www.independent.co.uk/topic/GoldenGlobes",
"http://www.independent.co.uk/arts-entertainment/films/news",
"http://www.independent.co.uk/author/jack-shepherd",
"http://www.independent.co.uk/topic/jeff-goldblum",
"http://www.independent.co.uk/author/harriet-agerholm",
"http://www.independent.co.uk/author/daniel-kraemer",
"http://www.independent.co.uk/author/tom-batchelor",
"http://www.independent.co.uk/topic/european-union",
"http://www.independent.co.uk/author/huw-jones",
"http://www.independent.co.uk/topic/fintech",
"http://www.independent.co.uk/news/business/analysis-and-features",
"http://www.independent.co.uk/author/ben-chu",
"http://www.independent.co.uk/topic/consumer-borrowing",
"http://www.independent.co.uk/topic/debt",
"http://www.independent.co.uk/money/moneydeals?icn=MSM_footer",
"http://www.independent.co.uk/commercial",
"http://www.independent.co.uk/author/peter-walker-0",
"http://www.independent.co.uk/author/ethan-spibey",
"http://www.independent.co.uk/topic/blood-donation",
"http://www.independent.co.uk/author/douglas-robertson",
"http://www.independent.co.uk/author/rachael-revesz",
"http://www.independent.co.uk/author/olivia-blair",
"http://www.independent.co.uk/author/helen-coffey",
"http://www.independent.co.uk/author/lauren-murray",
"http://www.independent.co.uk/topic/Chemicals",
"http://www.independent.co.uk/author/ian-johnston",
"http://www.independent.co.uk/author/independent-us-staff",
"http://www.independent.co.uk/topic/Earthquake",
"http://www.independent.co.uk/topic/India",
"http://www.independent.co.uk/author/maya-oppenheim",
"http://www.independent.co.uk/news/world/middle-east",
"http://www.independent.co.uk/author/samuel-osborne",
"http://www.independent.co.uk/topic/isis",
"http://www.independent.co.uk/news/world/americas/us-politics",
"http://www.independent.co.uk/author/alexandra-wilts",
"http://www.independent.co.uk/author/jeremy-b-white",
"http://www.independent.co.uk/topic/customs-and-border-protection",
"http://www.independent.co.uk/author/chloe-farand",
"http://www.independent.co.uk/topic/article-50",
"http://www.independent.co.uk/sport/football/transfers",
"http://www.independent.co.uk/author/sports-staff-2",
"http://www.independent.co.uk/topic/johanna-konta",
"http://www.independent.co.uk/author/luke-brown",
"http://www.independent.co.uk/sport/football/international",
"http://www.independent.co.uk/author/jonathan-liew",
"http://www.independent.co.uk/topic/Trevor_Bayliss",
"http://www.independent.co.uk/topic/England_cricket",
"http://www.independent.co.uk/author/rory-dollard-0",
"http://www.independent.co.uk/topic/Nemanja_Matic",
"http://www.independent.co.uk/topic/chelsea",
"http://www.independent.co.uk/author/sport-staff-0",
"http://www.independent.co.uk/sport/football/european",
"http://www.independent.co.uk/topic/RealMadrid",
"http://www.independent.co.uk/topic/january-transfer-window",
"http://www.independent.co.uk/topic/Philippe_Coutinho",
"http://www.independent.co.uk/topic/LiverpoolFC",
"http://www.independent.co.uk/topic/ASMonaco",
"http://www.independent.co.uk/author/jack-austin",
"http://www.independent.co.uk/topic/FcBarcelona",
"http://www.independent.co.uk/author/simon-hughes",
"http://www.independent.co.uk/sport/football/fa-league-cups",
"http://www.independent.co.uk/author/jim-daly",
"http://www.independent.co.uk/topic/ChelseaF.c.",
"http://www.independent.co.uk/author/jack-pitt-brooke",
"http://www.independent.co.uk/topic/arsènewenger",
"http://www.independent.co.uk/author/declan-warrington",
"http://www.independent.co.uk/topic/crystal-palace",
"http://www.independent.co.uk/property-news",
"http://www.independent.co.uk/property-news/buying",
"http://www.independent.co.uk/property-news/renting",
"http://www.independent.co.uk/mortgages",
"http://www.independent.co.uk/area-guides",
"http://www.independent.co.uk/area-guides/london",
"http://www.independent.co.uk/area-guides/commuter-hotspots",
"http://www.independent.co.uk/luxury",
"http://www.independent.co.uk/home-garden",
"http://www.independent.co.uk/home-garden/interiors",
"http://www.independent.co.uk/home-garden/food",
"http://www.independent.co.uk/home-garden/gardening",
"http://www.independent.co.uk/property-news/buying/new-homes",
"http://www.independent.co.uk/property-news/buying/first-time-buyers",
"http://www.independent.co.uk/property-news/buying/holiday-homes",
"http://www.independent.co.uk/luxury/property",
"http://www.independent.co.uk/luxury/celebrity-homes",
"http://www.independent.co.uk/luxury/interiors",
"http://www.independent.co.uk/luxury/interiors/design",
"http://www.independent.co.uk/area-guides/london/zone-1",
"http://www.independent.co.uk/author/chris-mandle",
"http://www.independent.co.uk/author/heather-saul",
"http://www.independent.co.uk/topic/nadia-murad",
"http://www.independent.co.uk/author/anne-marie-oconnor",
"http://www.independent.co.uk/topic/Israel",
"http://www.independent.co.uk/topic/bds",
"http://www.independent.co.uk/topic/palestinians",
"http://www.independent.co.uk/topic/israel-palestine-conflict",
"http://www.independent.co.uk/author/mythili-sampathkumar",
"http://www.independent.co.uk/topic/james-damore",
"http://www.independent.co.uk/author/cleve-r-wootson-jr-0",
"http://www.independent.co.uk/topic/Sweeteners",
"http://www.independent.co.uk/arts-entertainment/tv/reviews",
"http://www.independent.co.uk/author/sean-ogrady",
"http://www.independent.co.uk/topic/little-women",
"http://www.independent.co.uk/arts-entertainment/books/features",
"http://www.independent.co.uk/author/john-hamilton",
"http://www.independent.co.uk/topic/penguin-essentials",
"http://www.independent.co.uk/topic/ditchling-museum",
"http://www.independent.co.uk/profile?icn=_IND_culture_UAS",
"http://www.independent.co.uk/author/susie-mesure",
"http://www.independent.co.uk/author/adam-withnall",
"http://www.independent.co.uk/extras/indybest/house-garden/outside-eating",
"http://www.independent.co.uk/extras/indybest/house-garden/bbqs-accessories",
"http://www.independent.co.uk/extras/indybest/house-garden/garden-toys",
"http://www.independent.co.uk/extras/indybest/kids/baby-tech-essentials",
"http://www.independent.co.uk/extras/indybest/kids/pushchairs",
"http://www.independent.co.uk/extras/indybest/kids/travel",
"http://www.independent.co.uk/extras/indybest/kids/clothing-footwear",
"http://www.independent.co.uk/extras/indybest/kids/school-clothing-equipment",
"http://www.independent.co.uk/extras/indybest/kids/outside-toys-activities",
"http://www.independent.co.uk/extras/indybest/kids/gifts",
"http://www.independent.co.uk/extras/indybest/kids/books",
"http://www.independent.co.uk/extras/indybest/kids/furniture",
"http://www.independent.co.uk/extras/indybest/kids/sports",
"http://www.independent.co.uk/extras/indybest/books/non-fiction-books",
"http://www.independent.co.uk/extras/indybest/books/fiction-books",
"http://www.independent.co.uk/extras/indybest/books/cookbooks",
"http://www.independent.co.uk/voices/campaigns/GiantsClub",
"http://www.independent.co.uk/author/alex-dymoke",
"http://www.independent.co.uk/author/adam-lusher",
"http://www.independent.co.uk/topic/eu-referendum",
"http://www.independent.co.uk/author/gavin-cordon",
"http://www.independent.co.uk/author/ryan-wilkinson",
"http://www.independent.co.uk/topic/salad",
"http://www.independent.co.uk/author/julia-platt-leonard",
"http://www.independent.co.uk/topic/Recipes",
"http://www.independent.co.uk/topic/daily-recipe",
"http://www.independent.co.uk/topic/fried-rice",
"http://www.independent.co.uk/topic/food-and-drink",
"http://www.independent.co.uk/topic/daily-recipes",
"http://www.independent.co.uk/topic/Pork",
"http://www.independent.co.uk/profile?icn=_IND_life_UAS",
"http://www.independent.co.uk/author/ben-chapman",
"http://www.independent.co.uk/author/miles-dilworth",
"http://www.independent.co.uk/topic/entrepreneurs",
"http://www.independent.co.uk/author/hazel-sheffield",
"http://www.independent.co.uk/topic/etsy",
"http://www.independent.co.uk/business",
"http://www.independent.co.uk/author/sabrina-barr",
"http://www.independent.co.uk/author/staff-and-agencies",
"http://www.independent.co.uk/topic/Kansas",
"http://www.independent.co.uk/author/emily-shugerman",
"http://www.independent.co.uk/topic/antifa",
"http://www.independent.co.uk/author/christine-manby",
"http://www.independent.co.uk/author/emily-langer",
"http://www.independent.co.uk/author/martin-childs",
"http://www.independent.co.uk/author/lily-fletcher",
"http://www.independent.co.uk/author/tam-dalyell",
"http://www.independent.co.uk/topic/lord-jenkin",
"http://www.independent.co.uk/topic/MargaretThatcher",
"http://www.independent.co.uk/author/may-bulman",
"http://www.independent.co.uk/author/siobhan-fenton",
"http://www.independent.co.uk/topic/leo-varadkar",
"http://www.independent.co.uk/author/ben-kentish",
"http://www.independent.co.uk/topic/MichaelGove",
"http://www.independent.co.uk/topic/wild-animals",
"http://www.independent.co.uk/author/lydia-smith",
"http://www.independent.co.uk/author/simon-calder",
"http://www.independent.co.uk/topic/southern",
"http://www.independent.co.uk/topic/greater-anglia",
"http://www.independent.co.uk/author/harry-cockburn",
"http://www.independent.co.uk/author/clark-mindock",
"http://www.independent.co.uk/author/lucy-pasha-robinson",
"http://www.independent.co.uk/topic/grenfell-tower",
"http://www.independent.co.uk/topic/LondonFireBrigade",
"http://www.independent.co.uk/author/chris-baynes",
"http://www.independent.co.uk/arts-entertainment/music/news",
"http://www.independent.co.uk/author/christopher-hooton",
"http://www.independent.co.uk/arts-entertainment/interviews",
"http://www.independent.co.uk/topic/john-cena",
"http://www.independent.co.uk/author/clarisse-loughrey",
"http://www.independent.co.uk/topic/christmas-2017",
"http://www.independent.co.uk/author/sarah-young",
"http://www.independent.co.uk/author/roisin-oconnor",
"http://www.independent.co.uk/arts-entertainment/music/reviews",
"http://www.independent.co.uk/author/andy-gill",
"http://www.independent.co.uk/arts-entertainment/films/reviews",
"http://www.independent.co.uk/author/geoffrey-macnab",
"http://www.independent.co.uk/topic/all-the-money-in-the-world",
"http://www.independent.co.uk/author/ilana-kaplan",
"http://www.independent.co.uk/topic/golden-globes-2018",
"http://www.independent.co.uk/author/paul-waldman",
"http://www.independent.co.uk/topic/deep-throat",
"http://www.independent.co.uk/author/david-usborne",
"http://www.independent.co.uk/topic/DonaldTrump",
"http://www.independent.co.uk/arts-entertainment/tv/news",
"http://www.independent.co.uk/news/world/africa",
"http://www.independent.co.uk/topic/sahara",
"http://www.independent.co.uk/environment",
"http://www.independent.co.uk/author/josh-gabbatiss",
"http://www.independent.co.uk/topic/Astronauts",
"http://www.independent.co.uk/author/adam-watkins",
"http://www.independent.co.uk/topic/male-pill",
"http://www.independent.co.uk/author/jessica-morgan",
"http://www.independent.co.uk/topic/lavinia-woodward",
"http://www.independent.co.uk/topic/OxfordUniversity",
"http://www.independent.co.uk/author/glosswitch",
"http://www.independent.co.uk/author/tom-peck",
"http://www.independent.co.uk/topic/david-lidington",
"http://www.independent.co.uk/author/rachel-roberts-0",
"http://www.independent.co.uk/topic/SinnFein",
"http://www.independent.co.uk/topic/NorthernIreland",
"http://www.independent.co.uk/topic/james-brokenshire",
"http://www.independent.co.uk/topic/ChrisGrayling",
"http://www.independent.co.uk/topic/rmt"]

    #start_urls = ['https://www.express.co.uk/news/world/901647/European-Union-budget-Brexit-compensation-regions-Committee-of-the-Regions']


    custom_settings = {
    	'FEED_FORMAT': 'csv',
        'FEED_URI' : 'independent_links.csv'

        
    }

    def parse(self, response):
        #Extract product information
        #headlines = response.css('h1::attr(itemprop)').extract()
        #para = response.css('p::text').extract()
        category = ['news', 'showbiz', 'showbiz', 'comment', 'finance', 'travel', 'entertainment', 'life-style']
        link = response.css('a::attr(href)').extract()
        pattern = r"\/((\-|\+)?[0-9]+(\.[0-9]+)?)\/"
        regexp = re.compile(pattern)

        for item in zip(link):
            #print type(item[0])
            txt = str(item[0]).strip()
            if True:#for cat in category:
            	if regexp.search(txt):#'/'+cat in txt:
            		x = regexp.findall(txt)
		        maxlen = 0
                        for i in x[0]:
                            ml = len(i)
                            #print i, len(i)
                            if ml >maxlen:
                                maxlen = ml
                        #print txt, maxlen
                        if maxlen == 6:
            	            print txt, maxlen
            	            scraped_info = {
            	            'Links List' : txt,
            	            }
          		    yield scraped_info

