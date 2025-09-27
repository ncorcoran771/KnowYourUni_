
// Uniqueness constraints
CREATE CONSTRAINT FOR (s:Student) REQUIRE s.id IS UNIQUE;
CREATE CONSTRAINT FOR (c:Course) REQUIRE c.id IS UNIQUE;
CREATE CONSTRAINT FOR (d:Degree) REQUIRE d.id IS UNIQUE;
CREATE CONSTRAINT FOR (f:Faculty) REQUIRE f.id IS UNIQUE;
CREATE CONSTRAINT FOR (t:Term) REQUIRE t.id IS UNIQUE;
CREATE CONSTRAINT FOR (r:RequirementGroup) REQUIRE r.id IS UNIQUE;

// Indexes for common lookups
CREATE INDEX FOR (s:Student) ON (s.learningStyle);
CREATE INDEX FOR (c:Course) ON (c.department);
CREATE INDEX FOR (c:Course) ON (c.level);
CREATE INDEX FOR (d:Degree) ON (d.department);
CREATE INDEX FOR (d:Degree) ON (d.type);
CREATE INDEX FOR (t:Term) ON (t.type);
