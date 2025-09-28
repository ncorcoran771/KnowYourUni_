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

// --- MOCK DATA ---
const mockRelations: string[] = ["Course Prerequisites", "Student Clubs", "Faculty Departments"];

const mockGraphData: { [key: string]: GraphData } = {
  "Course Prerequisites": {
    nodes: [
      { id: "cs101", label: "Intro to CS", group: 1 },
      { id: "cs201", label: "Data Structures", group: 1 },
      { id: "cs202", label: "Algorithms", group: 1 },
      { id: "math151", label: "Calculus I", group: 2 },
      { id: "phys201", label: "Physics I", group: 3 },
    ],
    links: [
      { id: "l1", source: "math151", target: "cs101" },
      { id: "l2", source: "cs101", target: "cs201" },
      { id: "l3", source: "cs101", target: "cs202" },
      { id: "l4", source: "phys201", target: "math151" },
    ],
  },
  "Student Clubs": {
    nodes: [
      { id: "alice", label: "Alice", group: 1 },
      { id: "bob", label: "Bob", group: 1 },
      { id: "charlie", label: "Charlie", group: 1 },
      { id: "chess", label: "Chess Club", group: 2 },
      { id: "coding", label: "Coding Club", group: 2 },
      { id: "debate", label: "Debate Club", group: 2 },
    ],
    links: [
      { id: "l5", source: "alice", target: "chess" },
      { id: "l6", source: "alice", target: "coding" },
      { id: "l7", source: "bob", target: "coding" },
      { id: "l8", source: "charlie", target: "debate" },
      { id: "l9", source: "charlie", target: "chess" },
    ],
  },
  "Faculty Departments": {
    nodes: [
        { id: "smith", label: "Dr. Smith", group: 1 },
        { id: "jones", label: "Dr. Jones", group: 1 },
        { id: "lee", label: "Dr. Lee", group: 1 },
        { id: "davis", label: "Dr. Davis", group: 1 },
        { id: "cs", label: "CompSci", group: 2 },
        { id: "math", label: "Math", group: 2 },
        { id: "physics", label: "Physics", group: 2 },
    ],
    links: [
        { id: "l10", source: "smith", target: "cs" },
        { id: "l11", source: "jones", target: "cs" },
        { id: "l12", source: "jones", target: "math" },
        { id: "l13", source: "lee", target: "physics" },
        { id: "l14", source: "davis", target: "math" },
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
      .force("link", d3.forceLink<Node, Link>(data.links).id((d) => d.id).distance(120))
      .force("charge", d3.forceManyBody().strength(-300))
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

