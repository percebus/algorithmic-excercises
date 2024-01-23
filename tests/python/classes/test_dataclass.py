from dataclasses import dataclass, field
from typing import Any, ClassVar

import pytest
from hamcrest import assert_that, empty, equal_to, is_


def test__cls_property_list__assigned_to_list__raises_ValueError():
    with pytest.raises(ValueError) as oExceptionInfo:

        @dataclass
        class BadDataClass:
            __test__ = False

            # Rises ValueError:
            # SRC: https://docs.python.org/3/library/dataclasses.html#mutable-default-values
            items: list[Any] = []

    assert_that(str(oExceptionInfo.value), equal_to("mutable default <class 'list'> for field items is not allowed: use default_factory"))


def test__instance_field_list_with_default_list__raises_ValueError():
    with pytest.raises(ValueError) as oExceptionInfo:

        @dataclass
        class BadDataClass:
            __test__ = False

            items: list[Any] = field(default=[])

    assert_that(str(oExceptionInfo.value), equal_to("mutable default <class 'list'> for field items is not allowed: use default_factory"))


def test__instance_field_list_with_default_factory_list__works():
    @dataclass
    class GoodDataClass:
        __test__ = False

        items: list[Any] = field(default_factory=list)

    with pytest.raises(AttributeError) as oExceptionInfo:
        GoodDataClass.items

    # Does NOT have cls.items
    assert_that(str(oExceptionInfo.value), equal_to("type object 'GoodDataClass' has no attribute 'items'"))

    goodDataClass1 = GoodDataClass()
    assert_that(goodDataClass1.items, is_(empty()))

    goodDataClass1.items += [1, 2, 3]
    assert_that(goodDataClass1.items, is_(equal_to([1, 2, 3])))

    # New instance, new empty list
    goodDataClass2 = GoodDataClass()
    assert_that(goodDataClass2.items, is_(empty()))

    goodDataClass2.items += [4, 5, 6]
    assert_that(goodDataClass2.items, is_(equal_to([4, 5, 6])))
    assert_that(goodDataClass1.items, is_(equal_to([1, 2, 3])))


def test__ClassVar_VS_field_item__is_incorrect():
    @dataclass
    class BadNamingDataClass:
        __test__ = False

        # cls.items:
        # !!! WARNING !!! this does NOT work, nor will it Raise
        items: ClassVar[list[Any]] = []

        # self.items
        items: list[Any] = field(default_factory=list)

        @classmethod
        def init_cls(cls):
            cls.items: list[Any] = []

        @classmethod
        def get_class_items(cls):
            return cls.items

        def get_instance_items(self):
            return self.items

    with pytest.raises(AttributeError) as oExceptionInfo:
        #  WARNING this was NOT setup correctly
        BadNamingDataClass.items

    # Does NOT have cls.items
    assert_that(str(oExceptionInfo.value), equal_to("type object 'BadNamingDataClass' has no attribute 'items'"))

    # HACK now we are "initializing" (after the class has been initialized)
    # the "items" list that ClassVar should have done so.
    BadNamingDataClass.init_cls()
    BadNamingDataClass.items += [1, 2, 3]
    assert_that(BadNamingDataClass.items, is_(equal_to([1, 2, 3])))

    badNamingDataClass1 = BadNamingDataClass()

    # This obscures reference to cls.items
    badNamingDataClass1.items += [4, 5, 6]
    assert_that(badNamingDataClass1.items, is_(equal_to([4, 5, 6])))

    assert_that(badNamingDataClass1.get_class_items(), is_(equal_to([1, 2, 3])))
    assert_that(badNamingDataClass1.get_instance_items(), is_(equal_to([4, 5, 6])))

    badNamingDataClass2 = BadNamingDataClass()
    badNamingDataClass2.items += [7, 8, 9]
    BadNamingDataClass.items += [7, 8, 9]
    assert_that(badNamingDataClass2.items, is_(equal_to([7, 8, 9])))
    assert_that(badNamingDataClass1.items, is_(equal_to([4, 5, 6])))
    assert_that(BadNamingDataClass.items, is_(equal_to([1, 2, 3, 7, 8, 9])))


def test__ClassVar_VS_field_item_with_different_names__works():
    @dataclass
    class GoodNamingDataClass:
        __test__ = False

        # cls.cls_items
        cls_items: ClassVar[list[Any]] = []

        # self.obj_items
        obj_items: list[Any] = field(default_factory=list)

    assert_that(GoodNamingDataClass.cls_items, is_(empty()))

    # Access directly by the class
    GoodNamingDataClass.cls_items += [1, 2, 3]
    assert_that(GoodNamingDataClass.cls_items, is_(equal_to([1, 2, 3])))

    goodNamingDataClass1 = GoodNamingDataClass()
    assert_that(goodNamingDataClass1.obj_items, is_(empty()))
    assert_that(goodNamingDataClass1.cls_items, is_(GoodNamingDataClass.cls_items))

    goodNamingDataClass1.obj_items += [4, 5, 6]
    assert_that(goodNamingDataClass1.obj_items, is_(equal_to([4, 5, 6])))
    assert_that(goodNamingDataClass1.cls_items, is_(equal_to([1, 2, 3])))
    assert_that(GoodNamingDataClass.cls_items, is_(equal_to([1, 2, 3])))

    # New instance, new empty list
    goodNamingDataClass2 = GoodNamingDataClass()
    assert_that(goodNamingDataClass2.obj_items, is_(empty()))
    assert_that(goodNamingDataClass2.cls_items, is_(GoodNamingDataClass.cls_items))
    assert_that(goodNamingDataClass2.cls_items, is_(goodNamingDataClass1.cls_items))

    # Access cls from the instance
    goodNamingDataClass1.cls_items += [7, 8, 9]
    goodNamingDataClass2.obj_items += [7, 8, 9]
    assert_that(goodNamingDataClass2.obj_items, is_(equal_to([7, 8, 9])))
    assert_that(goodNamingDataClass1.obj_items, is_(equal_to([4, 5, 6])))
    assert_that(GoodNamingDataClass.cls_items, is_(equal_to([1, 2, 3, 7, 8, 9])))
