spin = input()
charge = input()
if spin != "1":
    if charge == "0":
        print("Muon Lepton")
    elif charge == "-1":
        print("Electron Lepton")
    elif charge == "2/3":
        print("Charm Quark")
    elif charge == "-1/3":
        print("Strange Quark")
else:
    print("Photon Boson")
