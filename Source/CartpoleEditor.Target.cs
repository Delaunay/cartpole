// BSD 3-Clause License Copyright (c) 2021, Pierre Delaunay All rights reserved.

using UnrealBuildTool;
using System.Collections.Generic;

public class CartpoleEditorTarget : TargetRules
{
	public CartpoleEditorTarget( TargetInfo Target) : base(Target)
	{
		Type = TargetType.Editor;
		DefaultBuildSettings = BuildSettingsVersion.V2;
		ExtraModuleNames.AddRange( new string[] { "Cartpole", "AIModule" } );
	}
}
