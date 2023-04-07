# python3


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables
        self.parents = list(range(n_tables))

    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False
 
        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size
        new_row_count = self.row_counts[src_parent] + self.row_counts[dst_parent]
        self.row_counts[src_parent] = 0
        self.row_counts[dst_parent] = new_row_count
        if new_row_count > self.max_row_count:
            self.max_row_count = new_row_count
        
        self.parents[src_parent] = dst_parent

        return True

    def get_parent(self, table):
        # find parent and compress path
        table_to_link = []
        while self.parents[table] != table:
            table_to_link.append(table)
            table = self.parents[table]
        for t in table_to_link:
            self.parents[t] = table
        return table


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
