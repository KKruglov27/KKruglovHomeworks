immutable_var = (14, 15.0, 'микрофон', 2, 2, ['микрофон', 'камера'], ['камера', 'микрофон'])
#immutable_var[0] = 15       # 'tuple' object does not support item assignment
#immutable_var[1] = 14.0     # 'tuple' object does not support item assignment
#immutable_var[2] = 'камера' # 'tuple' object does not support item assignment
#immutable_var.remove(15.0)  # 'tuple' object has no attribute 'remove'

                             # Мы не можем изменить объекты типа: int, float, str в immutable_var,
                             # данная переменная является кортежем, нельзя изменять значение объектов
                             # внутри кортежа, включая их удаление. Каждый объект в кортеже привязывается
                             # к определенному номеру, номер являет собой значение привязанного объекта.

#immutable_var[5][0] = immutable_var[6][0]  # (14, 15.0, 'микрофон', [2], [2], ['камера', 'камера'], ['камера', 'микрофон'])

                                            # Мы можем изменять данные внутри списков, что находятся в кортеже, поскольку
                                            # они являются объектами со своим внутренним набором изменяемых данных.

#immutable_var[5], immutable_var[6] = immutable_var[6], immutable_var[5]  # 'tuple' object does not support item assignment

                                                                          # Однако мы не можем, допустим, менять местами сами списки или
                                                                          # выполнять их слияние внутри кортежа, ведь каждый список
                                                                          # в кортеже так же является объектом cо своим номером,
                                                                          # а значит не изменяется самим кортежем и не может быть удален.

#immutable_var[3] = 2                 # 'tuple' object does not support item assignment
#immutable_var[3] = immutable_var[4]  # 'tuple' object does not support item assignment
#immutable_var[3] = immutable_var[3]  # 'tuple' object does not support item assignment
                                      # При попытке как-нибудь поменять значение объекта
                                      # в кортеже на идентичное, мы так же получим ошибку.
print(immutable_var)


mutable_list = [14, 15.0, 'микрофон', 2, 2, ['микрофон', 'камера'], ['камера', 'микрофон']]

mutable_list[5], mutable_list[6] = mutable_list[6], mutable_list[5] # = [14, 15.0, 'микрофон', [2], [2], ['камера', 'микрофон'], ['микрофон', 'камера']]
mutable_list[2] = 'камера'
mutable_list[0] = mutable_list[1] - mutable_list[0]
mutable_list.remove(15.0)
mutable_list[5] = mutable_list[4] + mutable_list[5]
mutable_list[5] = mutable_list[4] + mutable_list[5]
mutable_list[4] = mutable_list[4] * mutable_list[3]
print(mutable_list)