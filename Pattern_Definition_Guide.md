# Pattern Definition Guide

## CDL Recommended Patterns in RSE for HASS & Indigenous Research

## What is a Pattern?

### Foundational Definition

A **pattern** describes a recurring situation in our environment, and the recommendations that have proven useful in addressing it.

*Origin: This concept was pioneered by Christopher Alexander in architecture, who spoke of patterns capturing "a problem that occurs over and over again ... and the core of the solution to that problem." We've adapted his framing for research software engineering, where the recurring situation is often shaped by requirements (FAIR, CARE, ethical codes), principles (Indigenous data sovereignty, open science), goals (reproducibility, sustainability), or genuine technical concerns. A pattern in this repository captures any of these.*

### Pattern Structure

A pattern in this repository documents four **essential components**. Together they form the content of the pattern: they establish where and why the pattern applies (Context), what to do and why (Recommendations), how to do it in detail (Usage), and where and how it has been applied before (Implementations). Without any one of these, a pattern is incomplete. The document template places these four components within a broader structure that also includes Metadata, References, Citation, and Acknowledgments, sections that support discoverability, traceability, and attribution.

The template lays out all sections in the following order, with the four essential components marked:

1. **Pattern Metadata** — Pattern ID, slug, audience, keywords, status, authors, reviewers, version, last updated.
2. **Summary** *(contains Recommendations)*: one or two sentences naming the pattern's core purpose and the kinds of users it is intended for, followed by a Recommendation table. Each row pairs an imperative ("Do this") with the *Why?*: the risks it avoids and the benefits it brings.
3. **Context** *(essential component)*: the situation where the pattern is relevant: when it applies, when it does not, the resource constraints, and the kinds of projects it suits.
4. **Usage** *(essential component)*: the detailed guidance that expands the recommendations. Written as commands rather than narrative, with in-text links out to principles, related patterns, references, and how-to guides rather than embedded text. Diagrams may be used where they clarify structure.
5. **Implementations** *(essential component)*: known applications of the pattern, with background about how each was applied and the further contextual constraints about when you might want to use them.
6. **References**: organised into *Principles*, *Patterns*, *Models*, and *Other resources*, so each recommendation can be traced back to its source.
7. **Citation** and **Acknowledgments**: how to cite the pattern and who contributed to it.

The Recommendation table is the entry point; Usage is the working reference.

## Key Characteristics of Patterns

### Patterns are NOT Prescriptive Recipes

Patterns provide guidance and principles rather than rigid instructions. A pattern would not tell you exactly which technology to use; instead, it would propose a set of values and considerations to guide you toward a decision that is best for your particular application.

**Example:** - ❌ "Use PostgreSQL with these exact settings" - ✅ "Consider these factors when choosing between relational and document databases for your research data"

### Patterns Document Expert Knowledge

Patterns capture the accumulated wisdom and experience of experts who have navigated the same situation many times. They provide a valuable foundation for experience sharing and reuse across projects and teams.

### Patterns Form a Language

A **pattern language** is an organized and coherent set of patterns, each of which describes a recurring situation and the core of an approach. Patterns can reference and build upon each other, creating a rich vocabulary for discussing how to navigate complex situations.

## Patterns in Research Software Engineering

### Why Patterns Matter for RSE

Research software engineering operates within a complex research context that includes: - Navigating research agility and software sustainability - Managing sensitive or culturally significant data - Supporting reproducibility and FAIR principles - Enabling collaboration across diverse disciplines - Respecting Indigenous data sovereignty

Patterns help RSE practitioners by: 
- **Accelerating Development**: Avoid reinventing approaches for situations that recur 
- **Improving Quality**: Apply proven approaches 
- **Facilitating Communication**: Create shared vocabulary across teams 
- **Supporting Decision-Making**: Provide frameworks for evaluating options 
- **Enabling Learning**: Transfer knowledge from experienced to emerging RSEs

### Types of Patterns in RSE

Patterns in research software engineering can operate at multiple levels:

**Architectural Patterns** 
- High-level system organization. Example: Microservices vs monolithic architecture for research platforms

**Design Patterns** 
- Mid-level component interactions. Example: Observer pattern for real-time data updates

**Implementation Patterns** 
- Specific coding techniques. Example: Configuration management for multi-environment deployments

**Process Patterns** 
- Development workflows and practices. Example: Continuous integration for research software

**Organizational Patterns** 
- Team structures and collaboration models. Example: Embedded RSE support model

## Pattern Quality Criteria

### Good Patterns Should Be:

**1. Proven in Practice** Each recommendation comes from real-world experience and has been applied successfully more than once.

**2. Context-Specific** The Context section states clearly when the pattern applies and when it doesn't, including the resource constraints that shape it.

**3. Generative** The pattern supports different implementations rather than prescribing a single technology, leaving room for adaptation to local needs.

**4. Connected** The pattern references related patterns, building toward a coherent pattern language.

**5. Accessible** The pattern names its intended audiences and includes concrete implementations a reader can learn from.

## Pattern Evolution

Patterns evolve through use and refinement:

### Pattern Lifecycle

1.  **Discovery**: Recognise a recurring situation and an approach that has proven useful in it
2.  **Documentation**: Capture the pattern in structured form
3.  **Review**: Validate with community and experts
4.  **Publication**: Make available to broader community
5.  **Application**: Use in real projects
6.  **Refinement**: Update based on experience and feedback
7.  **Maturation**: Becomes well-understood and widely adopted


## Patterns in the CDL RSE Context

### Special Considerations for HASS & Indigenous Research

Patterns for this community must address:

**Cultural Sensitivity** 
- Indigenous data sovereignty principles (CARE) 
- Cultural protocols and permissions 
- Community consent and engagement 
- Traditional knowledge protection

**Disciplinary Diversity** 
- Wide range of research methods 
- Varied technical capabilities 
- Different data types and scales
- Interdisciplinary collaboration needs

**Ethical and Legal Complexity** 
- Privacy and consent management 
- Copyright and cultural rights 
- Long-term preservation responsibilities 
- Open access vs. access control

**Sustainability Challenges** 
- Project-based funding models 
- Limited technical resources 
- Knowledge continuity 
- Long-term maintenance


### Pattern Application Process

When applying a pattern to your research software project:

1.  **Match the situation**: Recognise that your situation matches the pattern's Context
2.  **Read the Recommendations**: Consider how each recommendation, and the reason paired with it, applies to your case
3.  **Adapt the Usage**: Tailor the pattern's Usage steps to your specific needs
4.  **Apply Thoughtfully**: Implement while monitoring outcomes
5.  **Reflect and Share**: Document your experience to help refine the pattern

## Further Reading

### Foundational Works

- Christopher Alexander, "A Pattern Language" (1977)
- Gang of Four, "Design Patterns: Elements of Reusable Object-Oriented Software" (1994)
- Martin Fowler, "Patterns of Enterprise Application Architecture" (2002)

### Research Software Engineering

- "Foundational Competencies and Responsibilities of a Research Software Engineer" (2023)
- Software Sustainability Institute resources
- FAIR4RS Principles documentation

### Indigenous Data Governance

- CARE Principles for Indigenous Data Governance
- Local Contexts: Traditional Knowledge Labels
- OCAP® Principles (Ownership, Control, Access, Possession)

## About This Guide

This guide was developed for the Community Data Lab Research Software Engineering Capacity Enhancement Project, supporting the HASS and Indigenous Research Data Commons.

**Version**: 1.0\
**Last Updated**: May 2026\
**License**: CC BY 4.0

For questions or contributions, please visit: \[Project Repository URL\]

## References

### Foundational Pattern Literature

Alexander, C., Ishikawa, S., & Silverstein, M. (1977). *A Pattern
Language: Towns, Buildings, Construction*. Oxford University Press.

Alexander, C. (1979). *The Timeless Way of Building*. Oxford University
Press.

Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design
Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley
Professional.

Fowler, M. (2002). *Patterns of Enterprise Application Architecture*.
Addison-Wesley Professional.

### Research Software Engineering

Goth, F., Alves, R., Braun, M., Castro, L. J., Chourdakis, G., Christ, S., Cohen, J., Erxleben, F., Grad, J., Hagdorn, M., Hodges, T., Juckeland, G., Kempf, D., Lamprecht, A., Linxweiler, J., Schwarzmeier, M., Seibold, H., Thiele, J. P., von Waldow, H. E., & Wittke, S. (2024). Foundational Competencies and Responsibilities of a Research Software Engineer. *F1000Research*, 13:1429. https://doi.org/10.12688/f1000research.157778.1

Software Sustainability Institute. (n.d.). *Research Software Engineering Resources*. Retrieved January 2026, from https://www.software.ac.uk/

### FAIR and CARE Principles

Chue Hong, N. P., Katz, D. S., Barker, M., Lamprecht, A., Martinez, C., Psomopoulos, F. E., Harrow, J., Castro, L. J., Gruenpeter, M., Martinez, P. A., & Honeyman, T. et al. (2022). FAIR Principles for Research Software version 1.0 (FAIR4RS Principles v1.0). *Research Data Alliance*. https://doi.org/10.15497/RDA00068

Barker, M., Chue Hong, N. P., Katz, D. S., Lamprecht, A., Martinez-Ortiz, C., Psomopoulos, F., Harrow, J., Castro, L. J., Gruenpeter, M., Martinez, P. A., & Honeyman, T. et al. (2022). Introducing the FAIR Principles for research software. *Scientific Data*, 9(1), 622. https://doi.org/10.1038/s41597-022-01710-x

Carroll, S. R., Garba, I., Figueroa-Rodríguez, O. L., Holbrook, J., Lovett, R., Materechera, S., Parsons, M., Raseroka, K., Rodriguez-Lonebear, D., Rowe, R., Sara, R., Walker, J. D., Anderson, J., & Hudson, M. (2020). The CARE Principles for Indigenous Data Governance. *Data Science Journal*, 19(1), 43. https://doi.org/10.5334/dsj-2020-043

Research Data Alliance International Indigenous Data Sovereignty Interest Group. (2019). *CARE Principles for Indigenous Data Governance*. The Global Indigenous Data Alliance. https://www.gida-global.org/care

### Additional Resources

Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A., ... & Mons, B. (2016). The FAIR Guiding Principles for scientific data management and stewardship. *Scientific Data*, 3(1), 160018. https://doi.org/10.1038/sdata.2016.18

Gabriel, R. P. (1996). *Patterns of Software: Tales from the Software Community*. Oxford University Press.

Buschmann, F., Meunier, R., Rohnert, H., Sommerlad, P., & Stal, M. (1996). *Pattern-Oriented Software Architecture, Volume 1: A System of Patterns*. John Wiley & Sons.

Attribution Statement: AIA Ph CeNc Hin R Claude4.6 v1.0

---

## Appendix: Patterns Compared to Other Knowledge Forms

Software patterns fulfill a different function to other forms of technical knowledge. Best practices prescribe what to do; principles state values; tutorials walk through specific tasks. Patterns do something different: they pair a recurring situation with the recommendations that have proven useful in it, leaving room for context and judgment. The comparisons below show where patterns sit relative to each of these forms.

### Patterns vs. Best Practices

| Patterns | Best Practices |
|---|---|
| Pair recommendations with the situations they suit | Prescribe specific actions |
| Context-dependent | Often presented as universal |
| Recognise context-dependence | Focus on optimal outcomes |
| Support multiple implementations | Recommend specific approaches |


### Patterns vs. Principles

| Patterns | Principles |
|---|---|
| Concrete and actionable | Abstract and guiding |
| Recommendations paired with reasons | Values and beliefs |
| Situational application | Universal application |
| “What” and “How” | “Why” |


### Patterns vs. Tutorials

| Patterns | Tutorials |
|---|---|
| Technology-agnostic where possible | Technology-specific |
| Focus on recurring situations | Focus on specific tasks |
| Multiple implementation options | Step-by-step instructions |
| Emphasise applicability | Emphasise completion |
