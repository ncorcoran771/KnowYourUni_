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
  [key:string]: any;
};

// Defines the structure of the data returned by our mock API
interface GraphData {
    nodes: Node[];
    links: Link[];
}


// --- API FUNCTIONS ---
/**
 * Fetches all available relation types from the FastAPI endpoint.
 * @returns A promise that resolves to an array of relation type strings.
 */
const fetchAllRelations = async (): Promise<string[]> => {
    console.log("Fetching all relation types from API...");
    try {
        const response = await fetch("/api/kg/relations");
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Failed to fetch relations:", error);
        // Return a default array or an empty one on error
        return ['Failed to load'];
    }
};

/**
 * Fetches graph data for a specific relationship type from the FastAPI endpoint.
 * @param relationType The type of relationship to fetch data for.
 * @returns A promise that resolves to the graph data.
 */
const fetchRelationships = async (relationType: string): Promise<GraphData> => {
    console.log(`Fetching relationships for: ${relationType} from API...`);
    // NOTE: The provided API endpoint /api/kg/graph requires a second integer parameter 'id2'.
    // As its purpose isn't defined in this context, a placeholder value of 0 is used.
    // This may need to be adjusted based on the actual API's requirements.
    const id2_placeholder = 0;
    const endpoint = `/api/kg/graph?id=${encodeURIComponent(relationType)}&id2=${id2_placeholder}`;

    try {
        const response = await fetch(endpoint);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data: GraphData = await response.json();
        return data;
    } catch (error) {
        console.error(`Failed to fetch graph for relation "${relationType}":`, error);
        // Return empty graph data on error to prevent the component from crashing.
        return { nodes: [], links: [] };
    }
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
        if (!selectedRelation || selectedRelation === 'Failed to load') {
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
                        Select data to form a knowledge graph:
                    </label>
                    <select
                        id="relation-select"
                        value={selectedRelation}
                        onChange={(e) => setSelectedRelation(e.target.value)}
                        className="p-2 border border-gray-300 rounded-md w-full max-w-xs"
                        disabled={loading || relations[0] === 'Failed to load'}
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

