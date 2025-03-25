from project import BaseArtifact
from project import ContemporaryArtifact
from project import RenaissanceArtifact
from project import BaseCollector
from project import Museum
from project import PrivateCollector


class AuctionHouseManagerApp:

    def __init__(self):
        self.artifacts = []
        self.collectors = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        self.is_artifact_valid(artifact_type)
        self.check_artifact_name(artifact_name)
        if artifact_type == "RenaissanceArtifact":
            new_artifact = RenaissanceArtifact(artifact_name, artifact_price, artifact_space)
        elif artifact_type == "ContemporaryArtifact":
            new_artifact = ContemporaryArtifact(artifact_name, artifact_price, artifact_space)
        else:
            raise ValueError("Invalid artifact type!")
        self.artifacts.append(new_artifact)
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    VALID_ARTIFACTS = ["RenaissanceArtifact", "ContemporaryArtifact"]
    @classmethod
    def is_artifact_valid(cls, artifact_type):
        if artifact_type not in cls.VALID_ARTIFACTS:
            raise ValueError("Unknown artifact type!")

    def check_artifact_name(self, artifact_name):
        if any(artifact.name == artifact_name for artifact in self.artifacts):
            raise ValueError(f"{artifact_name} has been already registered!")


    def register_collector(self, collector_type: str, collector_name: str):
        self.is_collector_valid(collector_type)
        self.check_collector_name(collector_name)
        if collector_type == "PrivateCollector":
            new_collector = PrivateCollector(collector_name)
        elif collector_type == "Museum":
            new_collector = Museum(collector_name)
        else:
            raise ValueError("Invalid collector type!")
        self.collectors.append(new_collector)
        return f"{collector_name} is successfully registered as a {collector_type}."


    VALID_COLLECTORS = ["Museum", "PrivateCollector"]
    @classmethod
    def is_collector_valid(cls, collector_type):
        if collector_type not in cls.VALID_COLLECTORS:
            raise ValueError("Unknown collector type!")

    def check_collector_name(self, collector_name):
        if any(collector.name == collector_name for collector in self.collectors):
            raise ValueError(f"{collector_name} has been already registered!")


    def perform_purchase(self, collector_name: str, artifact_name: str):

        collector = next((c for c in self.collectors if c.name == collector_name), None)
        if collector is None:
            raise ValueError("Artifact {artifact_name} is not registered to the auction!")
        artifact = next((a for a in self.artifacts if a.name == artifact_name), None)
        if artifact is None:
            raise ValueError("Artifact {artifact_name} is not registered to the auction!")
        if not collector.can_purchase(artifact.price, artifact.space_required):
            return "Purchase is impossible."

        collector.purchased_artifacts.append(artifact)
        collector.available_money -= artifact.price
        collector.available_space -= artifact.space_required
        self.artifacts.remove(artifact)

        return f"{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}."


    def remove_artifact(self, artifact_name: str):
        for artifact in self.artifacts:
            if artifact.name == artifact_name:
                self.artifacts.remove(artifact)
                return f"Removed {artifact.artifact_information()}"

        return "No such artifact."

    def fundraising_campaigns(self, max_money: float):
        collector_count = 0
        for collector in self.collectors:
            if collector.available_money <= max_money:
                collector.increase_money()
                collector_count += 1
        return f"{collector_count} collector/s increased their available money."

    def get_auction_report(self):
        sold_artifacts = sum(len(collector.purchased_artifacts) for collector in self.collectors)
        result = (
            f"**Auction statistics**\n"
            f"Total number of sold artifacts: {sold_artifacts}\n"
            f"Available artifacts for sale: {len(self.artifacts)}\n"
            f"***"
        )

        sorted_collectors = sorted(self.collectors, key=lambda c: (-len(c.purchased_artifacts), c.name) )
        for collector in sorted_collectors:
            result += f"\n{collector}"

        return result



    # @staticmethod
    # def _find_obj_by_name(obj_name, collection):
    #     return next((obj for obj in collection if obj.name == obj_name), None)