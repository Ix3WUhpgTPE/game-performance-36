class GamePerformance:
    def __init__(self):
        self.data = []
        self.cache = {}

    def add_score(self, player, score):
        if player in self.cache:
            self.cache[player] += score
        else:
            self.cache[player] = score
        self.data.append((player, score))

    def get_top_scores(self, n=10):
        sorted_scores = sorted(self.cache.items(), key=lambda x: x[1], reverse=True)
        return sorted_scores[:n]

    def clear_cache(self):
        self.cache.clear()

    def optimize_data_processing(self):
        unique_data = list(set(self.data))
        self.data = sorted(unique_data, key=lambda x: x[1], reverse=True)

    def performance_summary(self):
        return {"total_players": len(self.cache), "top_scores": self.get_top_scores()}