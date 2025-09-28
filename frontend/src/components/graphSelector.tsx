import React, { useEffect, useRef, FC, useState } from "react";
import * as d3 from "d3";

// --- TYPE DEFINITIONS ---
// Defines the structure for a node in the graph
type Node = {
  id: string;
  label?: string;
  group?: number;
  // D3 simulation properties
  x?: number;
  y?: number;
  vx?: number;
  vy?: number;
  fx?: number | null;
  fy?: number | null;
  [key: string]: any;
};

// Defines the structure for a link (edge) between nodes
type Link = {
  id: string;
  source: string | Node;
  target: string | Node;
  type?: string;
  [key: string]: any;
};

// Defines the structure of the graph data
interface GraphData {
  nodes: Node[];
  links: Link[];
}

// --- UMBC-SPECIFIC MOCK DATA ---
const mockRelations: string[] = ["UMBC CS Prerequisites", "UMBC Student Orgs", "UMBC Academic Departments"];

const mockGraphData: { [key: string]: GraphData } = {
  "UMBC CS Prerequisites": {
    nodes: [
      // Foundational Math & Stat
      { id: "math151", label: "MATH 151", group: 2 },
      { id: "math152", label: "MATH 152", group: 2 },
      { id: "math221", label: "MATH 221", group: 2 },
      { id: "stat355", label: "STAT 355", group: 5 },

      // Core CS 200 Level
      { id: "cmsc201", label: "CMSC 201", group: 1 },
      { id: "cmsc202", label: "CMSC 202", group: 1 },
      { id: "cmsc203", label: "CMSC 203", group: 1 },
      
      // Core CS 300 Level
      { id: "cmsc304", label: "CMSC 304", group: 3 },
      { id: "cmsc313", label: "CMSC 313", group: 3 },
      { id: "cmsc331", label: "CMSC 331", group: 3 },
      { id: "cmsc341", label: "CMSC 341", group: 3 },

      // Core CS 400 Level
      { id: "cmsc411", label: "CMSC 411", group: 4 },
      { id: "cmsc421", label: "CMSC 421", group: 4 },
      { id: "cmsc441", label: "CMSC 441", group: 4 },
      { id: "cmsc447", label: "CMSC 447", group: 4 },
    ],
    links: [
      // Math Path
      { id: "l1a", source: "math151", target: "math152" },
      { id: "l1b", source: "math151", target: "stat355" },
      { id: "l1c", source: "math152", target: "math221" },

      // CMSC 201 Path
      { id: "l2a", source: "math151", target: "cmsc201" },
      { id: "l2b", source: "cmsc201", target: "cmsc202" },

      // CMSC 203 Path
      { id: "l3a", source: "math151", target: "cmsc203" },
      
      // CMSC 300 Level Prerequisites
      { id: "l4a", source: "cmsc202", target: "cmsc313" },
      { id: "l4b", source: "cmsc202", target: "cmsc331" },
      { id: "l4c", source: "cmsc202", target: "cmsc341" },
      { id: "l4d", source: "cmsc203", target: "cmsc341" },
      { id: "l4e", source: "cmsc201", target: "cmsc304" },

      // CMSC 400 Level Prerequisites
      { id: "l5a", source: "cmsc313", target: "cmsc411" },
      { id: "l5b", source: "cmsc313", target: "cmsc421" },
      { id: "l5c", source: "cmsc341", target: "cmsc421" },
      { id: "l5d", source: "cmsc341", target: "cmsc441" },
      { id: "l5e", source: "cmsc341", target: "cmsc447" },
    ],
  },
  "UMBC Student Orgs": {
    nodes: [
      { id: "ashley", label: "Ashley", group: 1 },
      { id: "brandon", label: "Brandon", group: 1 },
      { id: "chris", label: "Chris", group: 1 },
      { id: "gamedev", label: "Game Dev Club", group: 2 },
      { id: "cyberdawgs", label: "Cyber Dawgs", group: 2 },
      { id: "swe", label: "SWE", group: 2 },
    ],
    links: [
      { id: "l8", source: "ashley", target: "swe" },
      { id: "l9", source: "ashley", target: "gamedev" },
      { id: "l10", source: "brandon", target: "cyberdawgs" },
      { id: "l11", source: "chris", target: "cyberdawgs" },
      { id: "l12", source: "chris", target: "gamedev" },
    ],
  },
  "UMBC Academic Departments": {
    nodes: [
        { id: "hrav", label: "Dr. Hrabowski", group: 1 },
        { id: "kalloy", label: "Dr. Kalpakis", group: 1 },
        { id: "adali", label: "Dr. Adali", group: 1 },
        { id: "csee", label: "CSEE", group: 2 },
        { id: "meche", label: "Mech Engineering", group: 2 },
        { id: "vart", label: "Visual Arts", group: 2 },
    ],
    links: [
        { id: "l13", source: "hrav", target: "csee" },
        { id: "l14", source: "kalloy", target: "csee" },
        { id: "l15", source: "adali", target: "csee" },
        { id: "l16", source: "hrav", target: "meche" },
    ]
  }
};

// --- MOCK API FUNCTIONS ---
/**
 * Simulates fetching all available relation types.
 * @returns A promise that resolves to an array of relation type strings.
 */
const fetchAllRelations = async (): Promise<string[]> => {
  console.log("Fetching all mock relation types...");
  return new Promise(resolve => {
    setTimeout(() => resolve(mockRelations), 500); // Simulate network delay
  });
};

/**
 * Simulates fetching graph data for a specific relationship type.
 * @param relationType The type of relationship to fetch data for.
 * @returns A promise that resolves to the graph data.
 */
const fetchRelationships = async (relationType: string): Promise<GraphData> => {
  console.log(`Fetching mock relationships for: ${relationType}...`);
  return new Promise(resolve => {
    setTimeout(() => resolve(mockGraphData[relationType] || { nodes: [], links: [] }), 500); // Simulate network delay
  });
};

// --- D3 Rendering Component ---
// This component is only responsible for rendering the SVG graph.
interface NodeGraphProps {
  data: GraphData;
}

const NodeGraph: FC<NodeGraphProps> = ({ data }) => {
  const ref = useRef<SVGSVGElement | null>(null);

  useEffect(() => {
    if (!ref.current || !data) return;

    const svg = d3.select(ref.current);
    svg.selectAll("*").remove(); // Clear old graph

    const width = 800;
    const height = 600;
    svg.attr("viewBox", `0 0 ${width} ${height}`);

    const simulation = d3
      .forceSimulation<Node>(data.nodes)
      .force("link", d3.forceLink<Node, Link>(data.links).id((d) => d.id).distance(50))
      .force("charge", d3.forceManyBody().strength(-200))
      .force("center", d3.forceCenter(width / 2, height / 2));

    const color = d3.scaleOrdinal(d3.schemeCategory10);

    const link = svg.append("g")
      .attr("stroke", "#999").attr("stroke-opacity", 0.6)
      .selectAll("line").data(data.links).join("line").attr("stroke-width", 2);

    const node = svg.append("g")
      .attr("stroke", "#fff").attr("stroke-width", 1.5)
      .selectAll("circle").data(data.nodes).join("circle")
      .attr("r", 15).attr("fill", d => color(d.group?.toString() ?? '0'))
      .call(d3.drag<SVGCircleElement, Node>()
        .on("start", (event, d) => {
          if (!event.active) simulation.alphaTarget(0.3).restart();
          d.fx = d.x; d.fy = d.y;
        })
        .on("drag", (event, d) => { d.fx = event.x; d.fy = event.y; })
        .on("end", (event, d) => {
          if (!event.active) simulation.alphaTarget(0);
          d.fx = null; d.fy = null;
        })
      );

    node.append("title").text((d: Node) => d.label ?? d.id);

    const labels = svg.append("g")
      .attr("class", "node-labels").attr("fill", "white") // Using white for better readability on colored nodes
      .attr("font-family", "sans-serif").attr("font-size", "10px")
      .selectAll("text").data(data.nodes).join("text")
      .attr("text-anchor", "middle").attr("dy", "0.35em")
      .text((d: Node) => d.label ?? d.id);

    simulation.on("tick", () => {
      link
        .attr("x1", (d: any) => (d.source as Node).x!)
        .attr("y1", (d: any) => (d.source as Node).y!)
        .attr("x2", (d: any) => (d.target as Node).x!)
        .attr("y2", (d: any) => (d.target as Node).y!);
      node.attr("cx", (d) => d.x!).attr("cy", (d) => d.y!);
      labels.attr("x", (d) => d.x!).attr("y", (d) => d.y!);
    });
    simulation.on("end", () => {
      simulation.stop();
      });

  }, [data]); // Re-run the effect whenever data changes

  return <svg ref={ref} width="100%" height="100%"></svg>;
}

// --- Main Application Component ---
// This component manages state, fetches data, and renders the UI shell.
const GraphD3: FC = () => {
  const [relations, setRelations] = useState<string[]>([]);
  const [selectedRelation, setSelectedRelation] = useState<string>('');
  const [graphData, setGraphData] = useState<GraphData | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  // Effect to fetch all relation types for the dropdown on initial mount
  useEffect(() => {
    fetchAllRelations().then(data => {
      setRelations(data);
      if (data.length > 0) {
        setSelectedRelation(data[0]); // Select the first relation by default
      } else {
        setLoading(false);
      }
    });
  }, []);

  // Effect to fetch graph data when the selected relation changes
  useEffect(() => {
    if (!selectedRelation) {
      setLoading(false);
      return;
    };

    setLoading(true);
    setGraphData(null); // Clear old data to show loading state
    fetchRelationships(selectedRelation)
      .then(data => {
        setGraphData(data);
      })
      .finally(() => {
        setLoading(false);
      });
  }, [selectedRelation]);

  return (
    <div className="bg-gray-100 font-sans p-4 min-h-screen flex items-center justify-center">
      <div className="w-full max-w-4xl bg-white rounded-lg shadow-md p-6">
        <h1 className="text-2xl font-bold text-gray-800 mb-4">University Relationship Visualizer</h1>
        <div className="mb-4">
          <label htmlFor="relation-select" className="block text-sm font-medium text-gray-700 mb-1">
            Select a relationship to visualize:
          </label>
          <select
            id="relation-select"
            value={selectedRelation}
            onChange={(e) => setSelectedRelation(e.target.value)}
            className="p-2 border border-gray-300 rounded-md w-full max-w-xs"
            disabled={loading}
          >
            {relations.map(rel => <option key={rel} value={rel}>{rel}</option>)}
          </select>
        </div>
        <div className="w-full h-[600px] border border-gray-200 rounded-md relative">
          {loading && (
            <div className="absolute inset-0 flex items-center justify-center bg-white/70">
              <div className="text-gray-600">Loading graph...</div>
            </div>
          )}
          {graphData && !loading && <NodeGraph data={graphData} />}
        </div>
      </div>
    </div>
  );
}

export default GraphD3;

