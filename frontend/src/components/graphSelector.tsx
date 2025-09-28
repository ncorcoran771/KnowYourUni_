import React from "react";
import CytoscapeComponent from "react-cytoscapejs";

interface DisplayGraphProps {
  elements: unknown[];
}
// use elements: any if this causes issues

export const DisplayGraph: React.FC<DisplayGraphProps> = ({ elements }) => {
  return (
    <CytoscapeComponent
      elements={elements}
      style={{ width: "100%", height: "600px" }}
      layout={{ name: "cose", animate: true }}
      stylesheet={[
        {
          selector: "node",
          style: {
            label: "data(label)",
            "text-valign": "center",
            "text-halign": "center",
            "background-color": "#0074D9",
            color: "#fff",
            width: 50,
            height: 50,
          },
        },
        {
          selector: "edge",
          style: {
            label: "data(label)",
            width: 2,
            "line-color": "#aaa",
            "target-arrow-color": "#aaa",
            "target-arrow-shape": "triangle",
            "curve-style": "bezier",
            "font-size": 9,
          },
        },
      ]}
      userZoomingEnabled
      userPanningEnabled
      boxSelectionEnabled
    />
  );
};

export default DisplayGraph;
