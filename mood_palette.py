# mood_palette.py

mood_color_data = {
    "happy": ["#FFEB3B", "#FFC107", "#FF9800", "#FF5722", "#E91E63"],
    "calm": ["#B2EBF2", "#B3E5FC", "#B2DFDB", "#DCEDC8", "#F0F4C3"],
    "retro": ["#EF6C00", "#F9A825", "#6D4C41", "#D7CCC8", "#FFF176"],
    "pastel": ["#FFD1DC", "#E0BBE4", "#957DAD", "#D291BC", "#FEC8D8"],
    "tech": ["#0f0f0f", "#1a1aff", "#33ccff", "#00b3b3", "#e6e6e6"],
    "muted": ["#A8B2AC", "#C3BABA", "#D8CFC4", "#E7D3C8", "#B0A295"],
    "vibrant": ["#F44336", "#E91E63", "#9C27B0", "#673AB7", "#3F51B5"],
    "nature": ["#2E7D32", "#66BB6A", "#A5D6A7", "#DCEDC8", "#F1F8E9"],
    "futuristic": ["#0F0F0F", "#00E5FF", "#1DE9B6", "#FF1744", "#D500F9"],
    "professional": ["#37474F", "#607D8B", "#90A4AE", "#CFD8DC", "#ECEFF1"],
    "happy": ["#FFE066", "#FFB347", "#FF6961", "#FF6F61", "#FFDAB9"],
    "sad": ["#5D737E", "#555B6E", "#889696", "#A2AEBB", "#D3D6DB"],
    "calm": ["#A3D2CA", "#5EAAA8", "#056676", "#EDF6F9", "#C3E0E5"],
    "creative": ["#FF77FF", "#B266FF", "#8E7DBE", "#D291BC", "#CBAACB"],
    "energetic": ["#FF5E5B", "#D7263D", "#F46036", "#FF9F1C", "#FFBF00"],
    "focused": ["#2C3E50", "#34495E", "#5D6D7E", "#85929E", "#BDC3C7"],
    "nature": ["#88B04B", "#A8E6CF", "#DCEDC1", "#FFD3B6", "#FFAAA5"],
    "forest": ["#355E3B", "#6B8E23", "#556B2F", "#8F9779", "#4F7942"],
    "spring": ["#FFB3BA", "#FFDFBA", "#FFFFBA", "#BAFFC9", "#BAE1FF"],
    "winter": ["#BFD8FF", "#A2C2E2", "#87A8D0", "#8FAADC", "#6D9DC5"],
    "summer": ["#FFD166", "#EF476F", "#06D6A0", "#118AB2", "#073B4C"],
    "autumn": ["#D2691E", "#CD853F", "#F4A460", "#FFDAB9", "#FFE4B5"],
    "romantic": ["#FFC0CB", "#FFB6C1", "#FF69B4", "#DB7093", "#C71585"],
    "vintage": ["#CDBE70", "#B5A642", "#D2B48C", "#A67B5B", "#8B4513"],
    "retro": ["#FF6F61", "#6B5B95", "#88B04B", "#F7CAC9", "#92A8D1"],
    "minimal": ["#FFFFFF", "#E0E0E0", "#BDBDBD", "#9E9E9E", "#424242"],
    "luxury": ["#BFAFB2", "#D4AF37", "#C0B283", "#E5C07B", "#A67B5B"],
    "elegant": ["#2C2C2C", "#8C8C8C", "#D3D3D3", "#E0E0E0", "#F5F5F5"],
    "soft": ["#E3FDFD", "#CBF1F5", "#A6E3E9", "#71C9CE", "#5FCDD9"],
    "bold": ["#D7263D", "#FF5700", "#F46036", "#1B1B1E", "#0047AB"],
    "dark": ["#0F0F0F", "#1C1C1E", "#2C2C2E", "#3A3A3C", "#48484A"],
    "light": ["#FFFFFF", "#FAFAFA", "#F0F0F0", "#E0E0E0", "#D0D0D0"],
    "neutral": ["#B0BEC5", "#CFD8DC", "#ECEFF1", "#90A4AE", "#78909C"],
    "warm": ["#FFB347", "#FFD700", "#FF7F50", "#FF6347", "#FF4500"],
    "cool": ["#00CED1", "#48D1CC", "#40E0D0", "#AFEEEE", "#E0FFFF"],
    "pastel": ["#FFD1DC", "#FFB7B2", "#FFDAC1", "#E2F0CB", "#B5EAD7"],
    "earthy": ["#836953", "#A67B5B", "#D2B48C", "#C19A6B", "#8B7355"],
    "neon": ["#39FF14", "#FF10F0", "#FF3131", "#00FFFF", "#F700FF"],
    "cyberpunk": ["#0F0F0F", "#FF00FF", "#00FFFF", "#FF1493", "#1E90FF"],
    "gamer": ["#111111", "#2D2D2D", "#FF5555", "#50FA7B", "#BD93F9"],
    "tech": ["#0F0F0F", "#1A1A1D", "#4E4E50", "#6F2232", "#950740"],
    "professional": ["#003366", "#005B96", "#6497B1", "#B3CDE0", "#E0E0E0"],
    "corporate": ["#35424A", "#1F618D", "#2471A3", "#D6DBDF", "#F2F3F4"],
    "study": ["#F7CAC9", "#92A8D1", "#F6E3B4", "#F5F5F5", "#A8D5BA"],
    "artist": ["#F67280", "#C06C84", "#6C5B7B", "#355C7D", "#F8B195"],
    "teacher": ["#89ABE3", "#EA738D", "#A1C349", "#F3D250", "#F78888"],
    "student": ["#FFDAC1", "#FFB7B2", "#FF9AA2", "#E2F0CB", "#C7CEEA"],
    "cool gray": ["#ECECEC", "#DADADA", "#B8B8B8", "#949494", "#707070"],
    "hot": ["#FF0000", "#FF4500", "#FF6347", "#FF7F50", "#FFA07A"],
    "ice": ["#E0FFFF", "#AFEEEE", "#ADD8E6", "#B0E0E6", "#87CEFA"],
    "space": ["#0B0C10", "#1F2833", "#45A29E", "#66FCF1", "#C5C6C7"],
    "sunset": ["#FF6E7F", "#FF9472", "#FFD194", "#FFF9B0", "#FCD8D4"],
    "sunrise": ["#FFE29F", "#FFA07A", "#FF7E5F", "#FF6E7F", "#FEB47B"],
    "desert": ["#EDC9Af", "#FFD39B", "#F4A460", "#C2B280", "#A67B5B"],
    "ocean": ["#0077BE", "#00BFFF", "#20B2AA", "#5F9EA0", "#40E0D0"],
    "sky": ["#87CEEB", "#B0E0E6", "#ADD8E6", "#E0FFFF", "#AFEEEE"],
    "rain": ["#A9A9A9", "#708090", "#778899", "#B0C4DE", "#D3D3D3"],
    "storm": ["#2F4F4F", "#36454F", "#4B4E6D", "#586875", "#696969"],
    "dreamy": ["#D8BFD8", "#E6E6FA", "#F0E68C", "#F5DEB3", "#FFE4E1"],
    "meditation": ["#A1E3D8", "#FCD5CE", "#F8EDEB", "#E0BBE4", "#D0F4DE"],
    "zen": ["#DDE5B6", "#F0EFEB", "#C1D0B5", "#A3B18A", "#E9EDC9"],
    "escape": ["#457B9D", "#A8DADC", "#F1FAEE", "#E63946", "#F4A261"],
    "nostalgic": ["#D3B88C", "#A1866F", "#8E806A", "#C5A880", "#BFA17D"],
    "inspired": ["#2A9D8F", "#E9C46A", "#F4A261", "#E76F51", "#264653"],
    "healing": ["#B5EAD7", "#E2F0CB", "#C7CEEA", "#FFDAC1", "#FFB7B2"],
    "festive": ["#D72638", "#3F88C5", "#F49D37", "#140F2D", "#F22B29"],
    "celebration": ["#FFD700", "#FF6347", "#FF69B4", "#FF8C00", "#FFA500"],
    "holiday": ["#F08080", "#FA8072", "#E9967A", "#FFA07A", "#FF7F50"],
    "playful": ["#FCF6B1", "#FFB3BA", "#BAE1FF", "#FFDFBA", "#FFFFBA"],
    "neutral warm": ["#E0C097", "#CBA135", "#D8B384", "#A67B5B", "#EDC9Af"],
    "neutral cool": ["#AEC6CF", "#D6EAF8", "#B0C4DE", "#D3D3D3", "#DDEBF7"],
    "earth": ["#A0522D", "#CD853F", "#DEB887", "#F5DEB3", "#FFE4B5"],
    "metallic": ["#BCC6CC", "#A9A9A9", "#C0C0C0", "#D3D3D3", "#E5E4E2"],
    "industrial": ["#3B3C36", "#6E6E6E", "#A9A9A9", "#C0C0C0", "#ECECEC"],
    "spiritual": ["#D7C0D0", "#F4E1D2", "#EADBC8", "#C3B091", "#A89F91"],
    "modern": ["#2B2D42", "#8D99AE", "#EDF2F4", "#EF233C", "#D90429"],
    "abstract": ["#FFADAD", "#FFD6A5", "#FDFFB6", "#CAFFBF", "#9BF6FF"],
    "funky": ["#FF00FF", "#00FFFF", "#FFFF00", "#00FF00", "#FF0000"],
    "dream": ["#CBAACB", "#FFB7B2", "#FFDAC1", "#E2F0CB", "#B5EAD7"],
    "love": ["#FFB6C1", "#FFC0CB", "#DC143C", "#FF69B4", "#C71585"],
    "adventure": ["#264653", "#2A9D8F", "#E9C46A", "#F4A261", "#E76F51"],
    "happy": ["#FFEB3B", "#FFC107", "#FF9800", "#FF5722", "#E91E63"],
    "calm": ["#B2EBF2", "#B3E5FC", "#B2DFDB", "#DCEDC8", "#F0F4C3"],
    "tech": ["#0F0F0F", "#1A1AFF", "#33CCFF", "#00B3B3", "#E6E6E6"],
    "pastel": ["#FFD1DC", "#E0BBE4", "#957DAD", "#D291BC", "#FEC8D8"],
    "warm": ["#FFB347", "#FF7F50", "#FF6F61", "#FFA07A", "#FFD700"],
    "cool": ["#00CED1", "#20B2AA", "#4682B4", "#5F9EA0", "#7FFFD4"],
    "muted": ["#A8B2AC", "#C3BABA", "#D8CFC4", "#E7D3C8", "#B0A295"],
    "soft": ["#FAE3E3", "#EAD5DC", "#D6CDEA", "#C8E3D4", "#F7F0D4"],
    "vibrant": ["#F44336", "#E91E63", "#9C27B0", "#673AB7", "#3F51B5"],
    "professional": ["#37474F", "#607D8B", "#90A4AE", "#CFD8DC", "#ECEFF1"],
    "modern": ["#212121", "#757575", "#BDBDBD", "#E0E0E0", "#FFFFFF"],
    "retro": ["#EF6C00", "#F9A825", "#6D4C41", "#D7CCC8", "#FFF176"],
    "futuristic": ["#0F0F0F", "#00E5FF", "#1DE9B6", "#FF1744", "#D500F9"],
    "luxury": ["#4A148C", "#880E4F", "#BF360C", "#212121", "#BFA27F"],
    "earthy": ["#A1887F", "#8D6E63", "#6D4C41", "#4E342E", "#3E2723"],
    "vintage": ["#CDB4DB", "#FFC8DD", "#FFAFCC", "#BDE0FE", "#A2D2FF"],
    "aesthetic": ["#DDBDD5", "#F7E1D7", "#A3C9A8", "#84B59F", "#69A297"],
    "neon": ["#DFFF00", "#FFBF00", "#FF7F50", "#DE3163", "#9FE2BF"],
    "corporate": ["#002F6C", "#005EB8", "#0072CE", "#00A9CE", "#00B2A9"],
    # Add more moods and themes below...
    "mystical": ["#6A0572","#AB83A1","#F0E6EF","#D291BC","#2E003E" ],
    "serene dusk": ["#A1C4FD","#C2E9FB","#BBD2C5","#536976","#292E49"],
    "candlelight": ["#FFD8A9","#FFE8C2","#FFB562","#F28F3B","#C8553D"],
    "foggy morning": ["#D6D6D6","#B0B0B0","#8E9AAF","#9CAFB7","#DCE0D9"],
    "lavender dreams": ["#D8B4E2","#E2C2F2","#EBDCFB","#F3E8FF","#BFA2DB"],
    "vintage denim": ["#3C4F76","#58728C","#AAB8C2","#E8E8E8","#3E505B"],
    "desert storm": ["#EDC9AF","#C2B280","#A67B5B","#8B7355","#6E5843" ],
    "emerald forest": ["#2E8B57","#228B22","#006400","#556B2F","#8F9779"],
    "bubblegum pop": ["#FF6F91","#FF9671","#FFC75F","#F9F871","#B5F44A"],
    "vaporwave": ["#FF71CE","#01CDFE","#05FFA1","#B967FF","#FFFB96"],
    "night sky": ["#0D1B2A","#1B263B","#415A77","#778DA9","#E0E1DD"],
    "golden hour": ["#FFDD00","#FDB813","#FFAB00","#FF8000","#FF5733"],
    "grayscale": ["#111111","#333333","#777777","#BBBBBB","#EEEEEE"],
    "mango lassi": ["#FFE17B","#FFD166","#FFB347","#FFA500","#FF8C00"],
    "blue lagoon": ["#00CED1","#20B2AA","#5F9EA0","#48D1CC","#00BFFF"],
    "cotton candy": ["#FEC8D8","#FFB6B9","#FFD3B4","#FFF5BA","#B5EAD7"],
    "cozy fire": ["#D7263D","#F46036","#FF9F1C","#FFBF00","#FC9E4F"],
    "herbal calm": ["#A8D5BA","#C0E3C6","#DFF3E3","#F0FFF1","#88B04B"],
    "metal twilight": ["#434343","#5A5A5A","#777777","#AAAAAA","#D3D3D3"],
    "rosewood": ["#65000B","#990F02","#C72C48","#FF6F61","#FF9999"],
    "fresh mint": ["#C1F4C5","#A8E6CF","#DCEDC1","#E0F7FA","#CCFF90"],
    "storybook": ["#FFC1FA","#B5EAEA","#EDF6E5","#F6DFEB","#DADADA"],
    "moody noir": ["#1C1C1E","#2C2C2E","#3A3A3C","#48484A","#636366"],
    "campfire night": ["#D2691E","#A0522D","#8B4513","#704214","#F4A460"],
    "daydream": ["#D0F4DE","#FDFCDC","#FFE9C6","#FEC8D8","#D8B4E2"],
    "abstract": ["#FFADAD", "#FFD6A5", "#FDFFB6", "#CAFFBF", "#9BF6FF"],
    "happy": ["#FFDDC1", "#FFABAB", "#FFC3A0", "#FF677D", "#D4A5A5"],
    "tech": ["#2C3E50", "#34495E", "#16A085", "#27AE60", "#2980B9"],
    "pastel": ["#FADADD", "#E0BBE4", "#D5AAFF", "#B5EAD7", "#C7CEEA"],
    "midnight": ["#0D1B2A", "#1B263B", "#415A77", "#778DA9", "#E0E1DD"]
    # Add more moods...
}
categorized_moods = {
    "Happy": [
         "playful", "sunny", "celebration", "holiday", "festive" , "happy"
    ],
    "Sad/Calm": [
         "serene dusk", "foggy morning", "lavender dreams", "meditation", "zen", "moody noir" , "sad",  "calm"
    ],
    "Tech & Futuristic": [
        "cyberpunk", "gamer", "vaporwave" ,"tech", "futuristic"
    ],
    "Pastel & Soft": [
         "cotton candy", "daydream", "storybook", "pastel", "soft"
    ],
    "Nature & Earthy": [
        "earth",  "desert", "emerald forest", "herbal calm" , "nature", "forest", "earthy"
    ],
    "Professional & Corporate": [
         "study", "teacher", "student","professional", "corporate"
    ],
    "Romantic & Love": [
        "dreamy", "candlelight" , "romantic", "love"
    ],
    "Dark & Moody": [
         "midnight", "moody noir", "space", "campfire night" , "dark", "storm"
    ],
    "Minimal & Neutral": [
         "neutral warm", "neutral cool", "grayscale" , "minimal" , "neutral"
    ],
    "Vibrant & Bold": [
         "funky", "neon", "hot" , "vibrant" , "bold"
    ],
    "Luxury & Elegant": [
         "metallic", "vintage", "rosewood", "luxury", "elegant"
    ],
    "Seasonal": [
        "spring", "summer", "autumn", "winter", "sunrise", "sunset"
    ],
    "Inspired & Creative": [
         "artist",  "adventure", "abstract", "creative" , "inspired"
    ],
    "Cool & Warm": [
        "ice", "blue lagoon", "mango lassi", "cool", "warm"
    ]
}



    

    