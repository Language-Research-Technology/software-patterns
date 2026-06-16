| Field                      | Value                                                                                                                                 |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Pattern ID                 | 1.2                                                                                                                                   |
| Title | **Implement Distributed license-based access control for data and services using Tiny Authorization Service**  |
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
| Implement the architectural pattern "Distributed license-based access control for data and services" | To get all the benefits of that pattern in a small system |
| Install the Tiny Authentication Service instead of building local user accounts and access control lists, or complex athentication rules into local applications.  | So that your application can scale up, you get the benefits of the parent pattern (long term sustainability, clear separation of data and applications, ability to swap out this implentation for a more enterprise-grade service later on) | 


## When this pattern applies

This pattern is suitable for use in small projects and proof of concept systems in place of a simple access control list strategy. It implement a minimal Authentication and Authorization service with the simplest possible configuration for orgnizations with limited resources. 


### When this pattern does not apply

Do not use this pattern:

- If there are trusted authorization systems already in place.
- When there are serious risks from data-leakage. In this case, use a Secure
  eResearch System or similar controlled environment.

### Usage

The main steps in implementing this pattern are to.

- Install the Tiny Authorization Service package in your application / service.
- RTFM
- Connect your repository or other resource providing app to the service by setting up the following congiguration:

TODO

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




