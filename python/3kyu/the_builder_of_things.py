# https://www.codewars.com/kata/5571d9fc11526780a000011a/python

class PredicateContainer:
    def __init__(self):
        self._predicates = {}

    def __getattr__(self, name):
        self._predicates[name] = True

    def set_false(self, name):
        self._predicates[name] = False

    def get_predicate_value(self, name):
        return self._predicates[name]

class FalsePredicateContainer:
    def __init__(self, predicate_container):
        self.predicate_container = predicate_container

    def __getattr__(self, name):
        self.predicate_container.set_false(name)

class Property:
    def __init__(self, thing):
        self.value = None
        self._thing = thing

    def __getattr__(self, name):
        self.value = name
        return self._thing

class PropertyContainer:
    def __init__(self, thing):
        self._properties = {}
        self._thing = thing

    def __getattr__(self, name):
        self._properties[name] = Property(self._thing)
        return self._properties[name]

    def get_property(self, name):
        return self._properties[name].value

    def has_property(self, name):
        return name in self._properties

class Verb:
    def __init__(self, subject):
        self.subject = subject

    def __call__(self, method, past_tense=None):
        self.method = method
        self.method.__globals__["name"] = self.subject
        self.past_tense = past_tense
        if not self.past_tense is None: self.history = []

    def run(self, *args):
        result = self.method(*args)
        if not self.past_tense is None:
            self.history.append(result)
        return result


class VerbContainer:
    def __init__(self, subject):
        self._verbs = {}
        self.subject = subject

    def __getattr__(self, name):
        self._verbs[name] = Verb(self.subject)
        return self._verbs[name]

    def has_verb(self, verb):
        return verb in self._verbs

    def get_verb(self, verb):
        return self._verbs[verb].run

    def has_history(self, past_tense):
        for _, verb in self._verbs.items():
            if verb.past_tense == past_tense: return True
        return False

    def get_history(self, past_tense):
        for _, verb in self._verbs.items():
            if verb.past_tense == past_tense: return verb.history


class Thing(object):
    def __init__(self, name):
        self.name = name
        self.is_a = PredicateContainer()
        self.is_not_a = FalsePredicateContainer(self.is_a)
        self.is_the = PropertyContainer(self)
        self._thing_containers = []
        self.can = VerbContainer(self.name)

    def __getattr__(self, name):
        if name.startswith("is_a_"):
            return self.is_a.get_predicate_value(name[len("is_a_"):])
        if name.startswith("is_"):
            return self.is_a.get_predicate_value(name[len("is_"):])
        if self.is_the.has_property(name):
            return self.is_the.get_property(name)
        if self.can.has_verb(name):
            return self.can.get_verb(name)
        if self.can.has_history(name):
            return self.can.get_history(name)
        if self.has_things(name):
            return self.get_things(name)

    def has_things(self, name):
        for thing_container in self._thing_containers:
            if thing_container.name == name: return True
        return False

    def get_things(self, name):
        for thing_container in self._thing_containers:
            if thing_container.name == name:
                return thing_container.things

    def has(self, number):
        thing_container = ThingContainer(number)
        self._thing_containers.append(thing_container)
        return thing_container

    def having(self, number):
        return self.has(number)

    @property
    def being_the(self):
        return self.is_the

    @property
    def and_the(self):
        return self.is_the

    def __repr__(self):
        return "Thing: %s" % self.name


class ThingContainer:
    def __init__(self, number):
        self.number = number

    def __getattr__(self, name):
        self.name = name
        thing_name = name if self.number == 1 else name[:-1]
        self._things = tuple(Thing(thing_name) for i in range(self.number))
        for thing in self._things:
            getattr(thing.is_a, thing_name)
        if self.number == 1: return self._things[0]
        else: return self

    @property
    def things(self):
        if self.number == 1:
            return self._things[0]
        else:
            return self._things

    @property
    def each(self):
        return Each(self._things)

    def __repr__(self):
        return "ThingContainer %s" % self.name

class Each:
    def __init__(self, items):
        self.items = items

    def __getattr__(self, name):
        return Each([getattr(item, name) for item in self.items])

    def __call__(self, *args):
        return Each([item(*args) for item in self.items])