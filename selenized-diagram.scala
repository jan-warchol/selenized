val plotW = 100
val plotH = 100

class Color(val name: String, val value: Int)

def genSvg(colors: List[Color]) = {
    <svg
       xmlns:dc="http://purl.org/dc/elements/1.1/"
       xmlns:cc="http://creativecommons.org/ns#"
       xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
       xmlns:svg="http://www.w3.org/2000/svg"
       xmlns="http://www.w3.org/2000/svg"
       xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
       xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
       width="100"
       height="100"
       id="svg2"
       version="1.1"
       inkscape:version="0.48.4 r9939"
       sodipodi:docname="lightness.svg">
      <defs
         id="defs4" />
      <sodipodi:namedview
         id="base"         pagecolor="#000000"
         bordercolor="#666666"
         borderopacity="1.0"
         inkscape:pageopacity="1"
         inkscape:pageshadow="2"
         inkscape:zoom="5.6568543"
         inkscape:cx="14.882487"
         inkscape:cy="45.948131"
         inkscape:document-units="px"
         inkscape:current-layer="layer1"
         showgrid="false"
         showguides="true"
         inkscape:guide-bbox="true"
         inkscape:window-width="799"
         inkscape:window-height="848"
         inkscape:window-x="0"
         inkscape:window-y="0"
         inkscape:window-maximized="0"
         inkscape:snap-object-midpoints="false" />
      <metadata
         id="metadata7">
        <rdf:RDF>
          <cc:Work
             rdf:about="">
            <dc:format>image/svg+xml</dc:format>
            <dc:type
               rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
            <dc:title />
          </cc:Work>
        </rdf:RDF>
      </metadata>
      <g
         inkscape:label="Layer 1"
         inkscape:groupmode="layer"
         id="layer1"
         transform="translate(0,0)">
        <rect
           style="fill:#a8bcc3;fill-opacity:1;stroke:none"
           id="fg-rect"
           width="100"
           height="25"
           x="0"
           y="0" />
        <rect
           style="fill:#154053;fill-opacity:1;stroke:none"
           id="bg-rect"
           width="100"
           height="50"
           x="0"
           y="25" />
        <rect
           style="fill:#000000;fill-opacity:1;stroke:none"
           id="black-rect"
           width="100"
           height="25"
           x="0"
           y="75" />
      </g>
        <g transform="translate(0,104) scale(1,-1)" >
           { for { (color, i) <- colors.zipWithIndex } yield {
           <rect
              style="fill:#fc5851;fill-opacity:1;fill-rule:evenodd;stroke:#154053;stroke-width:0.5;stroke-linecap:butt;stroke-linejoin:miter;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none"
              width="7.5"
              height="7.5"
              id={ color.name }
              x={ (i*plotW/colors.length).toString }
              y={ color.value.toString }
              />
           }}
      </g>
    </svg>
}

println("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>")
println(genSvg(List(new Color("foo", 50), new Color("bar", 80))))
