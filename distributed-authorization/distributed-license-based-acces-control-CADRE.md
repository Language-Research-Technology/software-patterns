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

- Concact your funding body to organise access to CILogon
- Make contact with the CADRE team and check that they are happy for you to go ahead with an implementation
- Work with the CADRE team to ensure there is an agreement in place for use of the service
- Code your application to follow the following protocols:
  -  Divide up resources by license
  -  Store or link licenses with resources (in the same storage object if possible for repositories)
  -  Identify authorization mechanisms availalble
      1. Automatic approval - by accepting terms/license and fill in form with more details if required
      2. Approval by a selected handler - An email will be sent to the approver with links to approve your access

#### Preparation

- Is your organisation in AAF/Edugain? If not contact your organisation's IT department
- Ask the governance body of your project/organisation who is allowed to login to filter the identity providers. CILogon will confugure the allowed identity providers
- Generate OIDC clients with CILogon
- Request an Organisation Ownership in CADRE
- Request an API key to CADRE
- Create the required assets to control access to your resource

#### In use

- Your application will use CILogon as an authentication interface and will use CADRE's API as an authorization interface to check if a logged in user has entitlements to each resource, each user is identified by an ID provided by CILogon.
- Entitlements can be revoked in CADRE management site
- Asset management in CADRE are immutable, once there is one request associated with a catalogue item.
- Each resource can have 1 or many handlers. Identify who is the handler for your resource so the handler can approve or deny an application
- CADRE is a modified version of [REMS](https://github.com/CSCfi/rems) Resource Entitlement Management System (REMS) is a tool for managing access rights to resources, such as research datasets. CADRE is based on REMS.



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




