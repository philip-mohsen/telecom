> ⚠ **Disclaimer:**
> This is a personal research project compiling publicly available information about telecom services. It does not include any internal data, confidential business strategies, or proprietary insights from any telecom company. All included information is sourced from publicly accessible materials, industry standards, and general telecom knowledge.
## Architecture
This project follows the principles of Clean Architecture and Domain-Driven Design (DDD) to ensure maintainability, testability, and flexibility.

### Layered Architecture
The project is structured into the following layers:
* **Domain Layer:**
    * Contains the core business logic, entities, value objects, and domain services.
    * Independent of any external frameworks or dependencies.
    * Located in the `src/<bounded_context>/domain/` and `src/shared/domain/` directories.
* **Application Layer:**
    * Contains use cases and application services that orchestrate the flow of data and logic between the domain and external systems.
    * Depends on the domain layer but not on the infrastructure or interfaces layers.
    * Located in the `src/<bounded_context>/application/` and `src/shared/application/` directories.
* **Infrastructure Layer:**
    * Contains the implementation details of external dependencies, such as databases, APIs, and logging.
    * Located in the `src/<bounded_context>/infrastructure/` and `src/shared/infrastructure/` directories.
* **Presentation Layer:**
    * Contains the code that interacts with the user, such as API endpoints and UI components (using Flask).
    * Depends on the application layer.
    * Located in the `src/<bounded_context>/presentation/` directories.
### Bounded Contexts

The project is divided into the following bounded contexts:
* **`technology_catalog`**
* **`service_catalog`**
* **`product_catalog`**
* **`device_management`**
* **`price_catalog`**
* **`offer_catalog`**

### Shared Code

Common code used across multiple bounded contexts is located in the `src/shared/` directory.

### Key Principles

* **Separation of Concerns:** Each layer and bounded context has a specific responsibility.
* **Dependency Inversion:** High-level modules do not depend on low-level modules; both depend on abstractions.
* **Testability:** The architecture facilitates easy testing of the core business logic.
* **Maintainability:** The clear separation of concerns makes the code easier to maintain and modify.
* **Flexibility:** The architecture allows for easy swapping of technologies or frameworks.
