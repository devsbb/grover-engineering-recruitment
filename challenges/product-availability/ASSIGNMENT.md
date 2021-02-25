# Product availability and reservations

You are tasked with making a reservation service which would be called during placing an order on Grover website. The initial step is to create a prototype service with a REST API endpoint that allows reserving assets for a list of products in the order or rejects the reservation request if these products are not in stock.

Glossary:
- Product – something you can order, e.g a smartphone
- Asset – a physical item that customer will receive, eg. a particular smartphone with a certain serial number
- Store – represents a geographical or other type of separation or product catalogs; allows to have a product available in store A and not in store B 
- Asset counters – a number of available assets in a particular store, eg. store A has 3 smartphones available to order

## Required features 

- Be able to reserve assets for an order
- Support multiple stores with asset counters per each store
- Be able to make assets available eg. for store A but not for store B

## Things we are looking for

- Scalability
- Attention to possible concurrency issues
- Separation of concerns
- Integration tests
- API design
- Domain modeling
- Error handling