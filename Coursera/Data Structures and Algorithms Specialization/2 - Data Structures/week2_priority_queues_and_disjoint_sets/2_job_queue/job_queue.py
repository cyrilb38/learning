# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

class Heap():
    def __init__(self, array):
        self.array = array
        self.heapify()

    def heapify(self):
            for i in range(len(self.array)//2, -1, -1):
                self.bubble_down(i)

    def bubble_down(self, indice):
        indice_min = None
        if (indice * 2 + 2) < len(self.array) :
            if (self.array[(indice * 2) + 1]["value"] < self.array[(indice * 2) + 2]["value"]):
                indice_min = (indice * 2 + 1)
            elif (self.array[(indice * 2) + 1]["value"] > self.array[(indice * 2) + 2]["value"]):
                indice_min = (indice * 2 + 2)
            elif (self.array[(indice * 2) + 1]["n_worker"] < self.array[(indice * 2) + 2]["n_worker"]):
                indice_min = (indice * 2 + 1)
            else :
                indice_min = (indice * 2 + 2)
        elif (indice * 2 + 1) < len(self.array) :
            indice_min = (indice * 2 + 1)

        if indice_min is not None and (self.array[indice_min]["value"] < self.array[indice]["value"]):     
            self.array[indice], self.array[indice_min] = self.array[indice_min], self.array[indice]
            self.bubble_down(indice_min)
        elif indice_min is not None and (self.array[indice_min]["value"] == self.array[indice]["value"]) and (self.array[indice_min]["n_worker"] < self.array[indice]["n_worker"]):
            self.array[indice], self.array[indice_min] = self.array[indice_min], self.array[indice]
            self.bubble_down(indice_min)

    def bubble_up(self, indice):
        indice_parent = (indice - 1) // 2
        if self.array[indice_parent]["value"] > self.array[indice]["value"]:
            self.array[indice], self.array[indice_parent] = self.array[indice_parent], self.array[indice]
            self.bubble_up(indice_parent)
        elif (self.array[indice_parent]["value"] == self.array[indice]["value"]) and (self.array[indice_parent]["n_worker"] > self.array[indice]["n_worker"]):
            self.array[indice], self.array[indice_parent] = self.array[indice_parent], self.array[indice]
            self.bubble_up(indice_parent)

    def get_min(self):
        return self.array[0]
    
    def change_min_priority(self, new_value):
        self.array[0]["value"] = new_value
        self.bubble_down(0)
    

def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    heap = Heap([{"n_worker" : x, "value" : 0} for x in range(n_workers)])
    # print(heap.array)
    for job in jobs:
        result.append(AssignedJob(heap.get_min()["n_worker"], heap.get_min()["value"]))
        heap.change_min_priority(heap.get_min()["value"] + job)
        # print(heap.array)

    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
