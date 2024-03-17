class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == 'type':
            typecount = 0
            for i in items:
                if i[0] == ruleValue:
                    typecount = typecount + 1
            return typecount

        elif ruleKey == 'color':
            colorcount = 0
            for i in items:
                if i[1] == ruleValue:
                    colorcount = colorcount + 1
            return colorcount

        elif ruleKey == 'name':
            namecount = 0
            for i in items:
                if i[2] == ruleValue:
                    namecount = namecount + 1
            return namecount
