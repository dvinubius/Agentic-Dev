# <External System>

## Role And Direction

- External system: `<name>`
- Direction: `<outbound dependency, inbound callback, or bidirectional>`
- Purpose: `<why this code interacts with it>`
- Code entry points: `<adapters, clients, handlers, or configuration paths>`

## Authoritative References

- `<official API, protocol, schema, or SDK documentation link and version>`

## Used Contract Surface

- Operations, endpoints, events, or resources: `<used subset>`
- Data consumed: `<fields or structures this code reads>`
- Data produced: `<fields or structures this code sends>`
- Internal mapping: `<internal types or domain concepts>`
- Ignored provider data: `<known unused fields or structures, or none>`

## Compatibility And Validation

- Required and optional data: `<assumptions>`
- Unknown-field behavior: `<ignored, retained, or rejected>`
- Version compatibility: `<supported versions or compatibility policy>`
- Validation boundary: `<where external data becomes trusted>`

## Operational Behavior

- Authentication and transport: `<mechanism and non-secret configuration>`
- Timeouts and retries: `<policy>`
- Rate limits and idempotency: `<constraints or none>`
- Failure translation and recovery: `<behavior>`

## Verification

- Contract tests or fixtures: `<paths or none>`
- Manual or external verification: `<procedure or none>`
