import pandas as pd


class PreProcess:
    # 0 = na / 1 = max / 2 = min / 3 = avg
    class FillMethod:
        def __init__(
            self, Int_FillMethod=None, Obj_FillMethod=None, Float_FillMethod=None
        ):
            self.Int_FillMethod = Int_FillMethod if Int_FillMethod is not None else 3
            self.Obj_FillMethod = Obj_FillMethod if Obj_FillMethod is not None else 0
            self.Float_FillMethod = (
                Float_FillMethod if Float_FillMethod is not None else 3
            )
            self.FillMethodTable = {
                "int64": self.Int_FillMethod,
                "float64": self.Float_FillMethod,
                "object": self.Obj_FillMethod,
            }

    def __init__(self, Int_FillMethod=None, Obj_FillMethod=None, Float_FillMethod=None):
        self.FillMethodWay = self.FillMethod(
            Int_FillMethod, Obj_FillMethod, Float_FillMethod
        )

    def s1_define(self, df):
        if df.empty:
            return False
        print(f"s1_define start with '{df.count}'")
        InputColumnType = []
        for column in df.columns:
            # if (df[column].dtype=="int64"):
            #     print(f"Column '{column}' has data type: int64")
            # elif (df[column].dtype=="float64"):
            #     print(f"Column '{column}' has data type: float64")
            # elif (df[column].dtype=="object"):
            #     print(f"Column '{column}' has data type: object")
            # else:
            #     print(f"Column '{column}' has data type: '{df[column].dtype}'")
            InputColumnType.append(df[column].dtype.name)
        print(f"s1_define end")
        print(f"")
        self.df = df
        self.InputColumnType = InputColumnType
        return self.InputColumnType.copy()

    def s2_adjustCol(self, AdjustColumnType=None):
        # print(f"s2_adjust from\t\t'{self.InputColumnType}'")
        if AdjustColumnType.count == self.InputColumnType.count:
            self.AdjustColumnType = (
                AdjustColumnType
                if AdjustColumnType is not None
                else self.InputColumnType
            )
            print(
                f"s2_adjust failed keep origin version\t\t\t'{self.AdjustColumnType}'"
            )
        else:
            self.AdjustColumnType = self.InputColumnType
        print(f"s2_adjust to\t\t\t'{self.AdjustColumnType}'")
        print(f"s2_adjust end")
        print(f"")
        return self.AdjustColumnType

    def s3_PreProcessing_Run(self):
        print("s3_PreProcessing_Run Start")
        print(f"Data frame col type From {self.InputColumnType}")
        print(f"Data frame col type   to {self.AdjustColumnType}")
        for i in range(len(self.InputColumnType)):
            print(f"s3_PreProcessing_Run for {i} col")
            DealWay = self.FillMethodWay.FillMethodTable[self.AdjustColumnType[i]]

            if self.InputColumnType[i] == self.AdjustColumnType[i]:
                if self.AdjustColumnType[i] == "object":
                    if DealWay == 0:
                        self.df.iloc[:, i] = self.df.iloc[:, i].fillna(0)
                    elif DealWay == 1:
                        self.df.iloc[:, i] = self.df.iloc[:, i].fillna(
                            self.df.iloc[:, i].max()
                        )
                    elif DealWay == 2:
                        self.df.iloc[:, i] = self.df.iloc[:, i].fillna(
                            self.df.iloc[:, i].min()
                        )
                    elif DealWay == 3:
                        self.df.iloc[:, i] = self.df.iloc[:, i].fillna(
                            self.df.iloc[:, i].mean()
                        )
            elif self.InputColumnType[i] == self.AdjustColumnType[i]:
                if self.AdjustColumnType[i] == "float":
                    self.df.iloc[:, i] = pd.to_numeric(self.df.iloc[:, i])
                    if DealWay == 0:
                        self.df.iloc[:, i] = self.df.iloc[:, i].fillna(0)
                    elif DealWay == 1:
                        self.df.iloc[:, i] = self.df.iloc[:, i].fillna(
                            self.df.iloc[:, i].max()
                        )
                    elif DealWay == 2:
                        self.df.iloc[:, i] = self.df.iloc[:, i].fillna(
                            self.df.iloc[:, i].min()
                        )
                    elif DealWay == 3:
                        self.df.iloc[:, i] = self.df.iloc[:, i].fillna(
                            self.df.iloc[:, i].mean()
                        )
            elif self.InputColumnType[i] == self.AdjustColumnType[i]:
                if self.AdjustColumnType[i] == "int":
                    self.df.iloc[:, i] = pd.to_numeric(self.df.iloc[:, i])
                    if DealWay == 0:
                        self.df.iloc[:, i] = self.df.iloc[:, i].fillna(0)
                    elif DealWay == 1:
                        self.df.iloc[:, i] = self.df.iloc[:, i].fillna(
                            self.df.iloc[:, i].max()
                        )
                    elif DealWay == 2:
                        self.df.iloc[:, i] = self.df.iloc[:, i].fillna(
                            self.df.iloc[:, i].min()
                        )
                    elif DealWay == 3:
                        self.df.iloc[:, i] = self.df.iloc[:, i].fillna(
                            self.df.iloc[:, i].mean()
                        )
            else:
                self.df.iloc[:, i] = self.df.iloc[:, i].fillna(0)
        return self.df
        print("s3_PreProcessing_Run OK")


p = PreProcess()
df_train = pd.read_csv("./train.csv")
adjCol = p.s1_define(df=df_train)
adjCol[4] = "int64"
adjCol = p.s2_adjustCol(adjCol)
p.s3_PreProcessing_Run()
