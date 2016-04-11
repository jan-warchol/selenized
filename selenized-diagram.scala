val plotW = 1200
val plotH = 600
val squareSize = 40
val squareHalf = squareSize/2.0
val squareBorder = 8

class Color(val name: String, val hexString: String, val luminance: Int)

def genSvg(bgColors: List[Color], fgColors: List[Color]) = {
    <svg
       xmlns="http://www.w3.org/2000/svg"
       xmlns:svg="http://www.w3.org/2000/svg"
       width={plotW.toString}
       height={plotH.toString}
       version="1.1"
       font-family="Signika, sans"
       font-size={(2*squareBorder).toString+"px"}>
       <style>
            @font-face {{
            font-family: 'Signika';
            font-style: normal;
            font-weight: 400;
            src: local('Signika'), local('Signika-Regular'), url(https://fonts.gstatic.com/s/signika/v6/q41y_9MUP_N8ipOH4ORRvw.woff2) format('woff2');
            unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2212, U+2215, U+E0FF, U+EFFD, U+F000;
            }}
            @font-face {{
            font-family: 'Signika';
            font-style: normal;
            font-weight: 700;
            src: local('Signika-Bold'), url(https://fonts.gstatic.com/s/signika/v6/7M5kxD4eGxuhgFaIk95pBfk_vArhqVIZ0nv9q090hN8.woff2) format('woff2');
            unicode-range: U+0000-00FF, U+0131, U+0152-0153, U+02C6, U+02DA, U+02DC, U+2000-206F, U+2074, U+20AC, U+2212, U+2215, U+E0FF, U+EFFD, U+F000;
            }}
       </style>{
            genBgColors(bgColors.sortBy(x => x.luminance))
        }{
            genFgColors(fgColors, bgColors.head)
    }</svg>
}

def genBgColors(colors: List[Color]) = {
    <g transform={"translate(0,"+plotH.toString+") scale(1,-1)"}>{
        for {color <- new Color("#000000", "000000", 0)::colors} yield {
            <rect
            style={"fill:#"+color.hexString+";fill-opacity:1;stroke:none"}
            width={ plotW.toString }
            height={ plotH.toString }
            x="0"
            y={ (color.luminance*plotH/100.0).toString } />
        }
    }</g>
}

def genFgColors(colors: List[Color], bgColor: Color) = {
    <g>{
        for {(color, i) <- colors.zipWithIndex} yield {
            val xcenter = (i+1)*plotW/(colors.length+1)
            val ycenter = color.luminance*plotH/100.0
            <g transform={"scale(1,-1) translate("+xcenter.toString+","+ycenter.toString+") scale(1,-1) translate(0, "+plotH.toString+")"}>
                <!-- group is translated to the center of square with some flipping for easier translation -->
                <g stroke={"#"+bgColor.hexString} stroke-width={squareBorder.toString}>
                    <rect
                        fill={"#"+color.hexString}
                        stroke={"#"+bgColor.hexString}
                        stroke-width={squareBorder.toString}
                        width={squareSize.toString}
                        height={squareSize.toString}
                        x={(-squareHalf).toString}
                        y={(-squareHalf).toString}/>
                    <line x1={(-squareHalf).toString} y1="0" x2={(squareBorder-squareHalf).toString} y2="0"/>
                    <line x1={squareHalf.toString} y1="0" x2={(squareHalf-squareBorder).toString} y2="0"/>
                </g>
                <text x="0" y="0" fill={"#"+bgColor.hexString} text-anchor="middle" dominant-baseline="central">{
                    color.luminance.toString
                }</text>
                <text x={(-squareSize*0.8).toString} y="0" fill={"#"+color.hexString} text-anchor="end" dominant-baseline="central" font-weight="bold" font-size={(0.8*squareSize).toString}
                    transform={"rotate(-90)"}>{
                    color.name
                }</text>
            </g>
        }
    }</g>
}

println("<?xml version=\"1.0\" encoding=\"UTF-8\"?>")
val bgColors = List(
    new Color("bg", "154053", 25),
    new Color("black", "245970", 35),
    new Color("fg", "a8bcc3", 75),
    new Color("white", "a8bcc3", 75),
    new Color("br_white", "c4d8df", 85)
)
val fgColors = List(
    new Color("bg", "154053", 25),
    new Color("black", "245970", 35),
    new Color("br_black", "7c95a0", 60),
    new Color("fg", "a8bcc3", 75),
    new Color("white", "a8bcc3", 75),
    new Color("br_white", "c4d8df", 85),
    new Color("red", "fc5851", 61),
    new Color("green", "78b93e", 69),
    new Color("yellow", "d8b033", 74),
    new Color("blue", "4e97f5", 61),
    new Color("magenta", "f16dc5", 65),
    new Color("cyan", "41c7b9", 73),
    new Color("br_red", "ff675d", 66),
    new Color("br_green", "85c74c", 74),
    new Color("br_yellow", "e7be42", 79),
    new Color("br_blue", "5ea4ff", 66),
    new Color("br_magenta", "ff7bd3", 70),
    new Color("br_cyan", "52d5c7", 78)
)
println(genSvg(bgColors, fgColors))
