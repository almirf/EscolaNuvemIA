from _typeshed import Incomplete

from braintree.graphql.inputs.customer_session_input import CustomerSessionInput

class UpdateCustomerSessionInput:
    def __init__(
        self, session_id: str, merchant_account_id: str | None = None, customer: CustomerSessionInput | None = None
    ) -> None: ...
    def to_graphql_variables(self) -> dict[Incomplete, Incomplete]: ...
    @staticmethod
    def builder(session_id: str): ...

    class Builder:
        def __init__(self, session_id: str) -> None: ...
        def merchant_account_id(self, merchant_account_id): ...
        def customer(self, customer): ...
        def build(self): ...
