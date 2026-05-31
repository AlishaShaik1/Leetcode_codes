class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        x=mass

        for i in asteroids:
            if i>x:
                return False
            x+=i
        return True
                