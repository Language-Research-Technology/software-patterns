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

This implementation is suitable for small research projects

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

This pattern is implemented in three phases: establish prerequisites, configure external services, then integrate authorization checks into your application.

1. Confirm prerequisites

- Confirm your project is in scope for national research infrastructure.
- Confirm your organisation can use AAF/eduGAIN (or identify an alternative path with your IT team).
- Confirm there is no existing trusted authorization system that should be reused.

Outcome: You have governance and identity preconditions in place.

2. Engage required service providers

- Contact your funding body to organise access to CILogon.
- Contact the CADRE team to confirm suitability and onboarding.
- Put service-use agreements in place with CADRE.

Outcome: You have approved access to both authentication and authorization services.

3. Configure identity and authorization services

- Configure allowed identity providers in CILogon.
- Generate OIDC clients in CILogon for your application.
- Request CADRE organisation ownership and API credentials.
- Define CADRE assets and handlers for each protected resource.

Outcome: Your external authN/authZ dependencies are configured.

4. Implement application integration

- Group resources by license (access policy)
- Store or link license metadata to each resource.
- For each request, authenticate users through CILogon and authorize via CADRE entitlement checks.
- Support approval paths:
  1. Self-service approval (accept terms and submit required details).
  2. Handler approval (designated approver receives and processes requests).

Outcome: Access decisions are enforced consistently by external services.

5. Operate and maintain

- Revoke entitlements through the CADRE management interface as needed.
- Keep handler assignments current for each resource.
- Plan around CADRE asset immutability when requests already exist.

Outcome: Ongoing access governance remains auditable and maintainable.

#### Preparation

- Confirm your organisation can use AAF/eduGAIN. If not, work with your IT team on federation onboarding.
- Confirm with project governance which identity providers should be allowed for login.
- Ask CILogon to configure those allowed identity providers.
- Generate OIDC clients in CILogon for your application.
- Request organisation ownership and API credentials in CADRE.
- Define CADRE assets needed for your access model:
  - Catalogue items
  - Resources
  - Forms
  - Workflows
  - Licenses

#### In use

- Use CILogon for authentication and the CADRE API for authorization checks on each resource request.
- Identify each user by the stable ID provided by CILogon.
- Revoke entitlements through the CADRE management interface when access should end.
- Assign one or more handlers per resource to review and approve or deny access requests.
- Plan for CADRE immutability rules: assets become effectively immutable once requests are associated with a catalogue item.
- CADRE is a modified version of the Resource Entitlement Management System ([REMS](https://github.com/CSCfi/rems)), used to manage access rights to resources such as research datasets.

# References

### Principles

[PILARS] <-- TODO: should we have a set of standard refs like this that get added to the pipeline so markdown links just work?

### Patterns

 [Distributed license-based access control for data and services](./distributed-license-based-acces-control.md)

### Models

[HASS&I RDM Concept Model]

### Other resources

- [CADRE documentation](https://documentation.cadre.ada.edu.au)
- [ARDC CADRE](https://ardc.edu.au/project/cadre/)
- [REMS](https://github.com/CSCfi/rems)


## Citation

## Acknowledgments


# TODO




