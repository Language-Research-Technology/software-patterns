| Field                      | Value                                                                                                                                 |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Pattern ID                 | 1.2                                                                                                                                   |
| Title | **Implement Distributed license-based access control for data and services using CADRE**  |
| Slug                       | distributed-authorization                                                                                                             |
| Audience Includes (hidden) | HASS RSEs (building systems); University IT / eResearch Teams;                                                                        |
| Keywords                   | authentication, federated identity, SSO, single sign-on, AAF, CILogon, Identity Provider, OIDC, OAuth2, AARC, research infrastructure |
| Status                     | Draft                                                                                                                                 |
| Category | Authentication and Authorization |
| Type                       | Implementation                                                                                                                          |
| Implements      | 1.0.  |
| Author                     | Peter Sefton                                                                                                                          |
| Last Updated               | 2026-05-20                                                                                                                            |

# Summary

This pattern implements the architectural pattern Distributed license-based access control for data and services.

This implementation is suitable for small ...

The same restrictions on types of data it should be used for apply as for the architectural pattern.



The same pattern can be used for access to services, such as computing.


| Recommendation                                                                                                                                                                                      | Why?                                                                                                                                                                                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Implement the architectural pattern "Distributed license-based access control for data and services" using the National (Australian) CADRE service | To get all the benefits of that pattern in a national research infrastructure contexxt  |
| Use CADRE as an Authorization Service alongside CILogon as an Authentication service  |  Per the Architectual pattern, you do not need to maintain user details or complex authorization logic in your service  | 


## When this pattern applies

This pattern is suitable for use in national research infrastructure projects.


### When this pattern does not apply

Do not use this pattern:

- If there are trusted authorization systems already in place.
- When there are serious risks from data-leakage. In this case, use a Secure
  eResearch System or similar controlled environment.

### Usage

The main steps in implementing this pattern are to.

- Make contact with the CADRE team and check that they are happy for you to go ahead with an implementation
- Work with the CADRE team to ensure there is an agreement in place for use of the service
- Code your application to follow the following protocols:


  -  Divide up resources by license
  -  Store licenses with resources (in the same storage object if possible for repositories)
  - blah blah 
  

#### Preparation



#### In use



# References

### Principles

[PILARS] <-- TODO: should we have a set of standard refs like this that get added to the pipeline so markdown links just work?

### Patterns

### Models

[HASS&I RDM Concept Model]

### Other resources

## Citation

## Acknowledgments


# TODO




